from flask import Flask, jsonify, request
import mysql.connector as mysql
import os, sys
from typing import Tuple, Dict, List


app = Flask(__name__)
DB_CONFIG = {}

HOUR = 0
DAY = 1
DISTANCE = 2
PARENT = 3
PARENT_NODE = 0
PARNET_FLIGHT_ID = 1
CITY = 4
HOPS = 5


def database_context(callback):
    global DB_CONFIG
    conn = mysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    result = callback(cursor, conn)
    cursor.close()
    conn.commit()
    conn.close()

    return result


def parseChildren(children, crtNode):
    result = []
    if children is None:
        return result
    
    hops = crtNode[-1]
    for child in children:
        cId, cDest, cHour, cDay, cDuration = child[0], child[1], child[2], child[3], child[4]
        cDist = 24 * cDay + cHour + cDuration
        newNode = (cHour, cDay, cDist, [crtNode, cId], cDest, hops - 1)
        result.append(newNode)
    
    return result


def format_string_for_query_list(l: list):
    return ','.join(['%s'] * len(l))


@app.route("/getOptimalRoute/<string:departure>/<string:dest>/<int:maxFlights>/<int:departureDay>", methods=["GET"])
def getOptimalRoute(departure, dest, maxFlights, departureDay):
    def callback(cursor: mysql.cursor.MySQLCursor, conn: mysql.connection.MySQLConnection):
        if maxFlights == 0:
            return jsonify("")

        try:
            crtNode = (0, departureDay, 0, None, departure, maxFlights)
            q = [crtNode]
            optimal = None
            while len(q) > 0:
                crtNode = q.pop(0)
                hour, day, _, __, city, hops = crtNode
                if hops == 1: # only one flight left, it should be to the destination
                    cursor.execute(f'SELECT FlightId, Destination, DepartureHour, DepartureDay, Duration ' \
                                   f'FROM Flight ' \
                                   f'WHERE (DepartureDay >= {day} or (DepartureDay = {day} and DepartureHour >= {hour})) and Departure = \'{city}\' and Destination = \'{dest}\'')
                    candidates = parseChildren(cursor.fetchall(), crtNode)
                    if optimal is not None:
                        candidates = list(filter(lambda child: child[DISTANCE] < optimal[DISTANCE], candidates))
                    if len(candidates) > 0:
                        optimal = min(candidates, key=lambda child: child[DISTANCE])
                else:
                    cursor.execute(f'SELECT FlightId, Destination, DepartureHour, DepartureDay, Duration ' \
                                   f'FROM Flight ' \
                                   f'WHERE (DepartureDay >= {day} or (DepartureDay = {day} and DepartureHour >= {hour})) and Departure = \'{city}\'')
                    result = cursor.fetchall()
                    for child in parseChildren(result, crtNode):
                        # don't bother with children that are on a longer route than the current optimal
                        if optimal is None or child[DISTANCE] < optimal[DISTANCE]:
                            if child[CITY] == dest:
                                optimal = child
                            else:
                                q.append(child)
            if optimal is None:
                return "No route found."
            
            details = []
            flightIds = []
            while optimal[PARENT] is not None:
                optimal = optimal[PARENT]
                flightIds.insert(0, optimal[PARNET_FLIGHT_ID])
                optimal = optimal[PARENT_NODE]
            
            for flightId in flightIds:
                cursor.execute(f'SELECT Departure, Destination, DepartureDay, DepartureHour, Duration ' \
                               f'FROM Flight WHERE FlightId = {flightId}')
                result = cursor.fetchone()
                if result is None:
                    continue

                details.append(f"Flight from {result[0]} to {result[1]} on day {result[2]} at {result[3]}:00 takes {result[4]} hours.")
            
            return {'human_strings': details, 'flightIds': flightIds}
        except mysql.Error:
            return ""
    
    return jsonify(database_context(callback))


@app.route("/bookTicket", methods=["POST"])
def bookTicket():
    if 'flightIds' not in request.json:
        return jsonify("")
    ids = [int(id) for id in request.json['flightIds']]
    def callback(cursor: mysql.cursor.MySQLCursor, conn: mysql.connection.MySQLConnection):
        try:
            format_str = format_string_for_query_list(ids)
            cursor.execute('SELECT FlightId, AvailableSeats, BookedSeats FROM Flight WHERE FlightId IN (%s)' % format_str, tuple(ids))
            flights = [{'id': row[0], 'available': row[1], 'booked': row[2]} for row in cursor.fetchall()]

            if any(filter(lambda f: f['booked'] >= 1.1 * f['available'], flights)):
                return "No more seats on one of the choosen flights."
            
            cursor.execute('UPDATE Flight SET BookedSeats = BookedSeats + 1 WHERE FlightId IN (%s)' % format_str, tuple(ids))
            cursor.execute('INSERT INTO Reservation VALUES()')
            reservationId = cursor.lastrowid

            for id in ids:
                cursor.execute(f'INSERT INTO ReservationFlight (ReservationId, FlightId) VALUES({reservationId}, {id})')

            return reservationId
        except mysql.Error:
            conn.rollback()
            return ""
    
    return jsonify(database_context(callback))


@app.route("/buyTicket", methods=["POST"])
def buyTicket():
    if 'reservationId' not in request.json:
        return jsonify("")

    reservationId = int(request.json['reservationId'])
    def callback(cursor: mysql.cursor.MySQLCursor, conn: mysql.connection.MySQLConnection):
        try:
            cursor.execute(f'SELECT WasBought FROM Reservation WHERE ReservationId = {reservationId}')
            wasBought = cursor.fetchone()
            if wasBought is None:
                return ["Reservation doesn't exist."]
            if wasBought[0] > 0:
                return ["A ticket for this reservation was already bought."]
            
            cursor.execute(f'SELECT FlightId FROM ReservationFlight WHERE ReservationId = {reservationId}')
            flightIds = cursor.fetchall()
            if flightIds is None:
                return ["No flights associated with the reservation."]
            
            flightIds = [id[0] for id in flightIds]
            format_str = format_string_for_query_list(flightIds)
            cursor.execute('SELECT FlightId, AvailableSeats, BoughtSeats, Departure, Destination, DepartureHour, DepartureDay, Duration FROM Flight WHERE FlightId IN (%s)' % format_str, tuple(flightIds))
            flights = [{'id': row[0], 'available': row[1], 'bought': row[2], 'departure': row[3], 'dest': row[4], 'hour': row[5], 'day': row[6], 'duration': row[7]}
                for row in cursor.fetchall()]

            if any(filter(lambda f: f['bought'] >= f['available'], flights)):
                return ["No more seats on one of the flights."]

            cursor.execute('UPDATE Flight SET BoughtSeats = BoughtSeats + 1 WHERE FlightId IN (%s)' % format_str, tuple(flightIds))
            cursor.execute(f'UPDATE Reservation SET WasBought = true WHERE ReservationId = {reservationId}')

            details = []
            for f in flights:
                details.append(f"Flight from {f['departure']} to {f['dest']} on day {f['day']} at {f['hour']}:00 takes {f['duration']} hours.")
            return details
        except mysql.Error:
            conn.rollback()
            return ""
    
    return jsonify(database_context(callback))


def main():
    global DB_CONFIG
    DB_CONFIG = {
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'port': os.environ['DB_PORT'],
        'database': os.environ['DB_NAME']
    }
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()