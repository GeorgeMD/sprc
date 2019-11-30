import mysql.connector as mysql
import os


POSSIBLE_ACTIONS = "AddFlight <Departure> <Destination> <DepartureDay> <DepartureHour> <Duration> <NumberOfSeats> <FlightId>\nRemoveFlight <FlightId>"
DB_CONFIG = {}


def database_context(callback: callable):
    global DB_CONFIG
    conn = mysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    callback(cursor)
    cursor.close()
    conn.commit()
    conn.close()


def AddFlight(Departure: str, Destination: str, DepartureDay: int, DepartureHour: int, 
              Duration: int, NumberOfSeats: int, FlightId: int):
    DepartureDay = int(DepartureDay)
    DepartureHour = int(DepartureHour)
    Duration = int(Duration)
    NumberOfSeats = int(NumberOfSeats)
    FlightId = int(FlightId)
    if DepartureDay < 1 or DepartureDay > 365:
        raise ValueError("Departure day must be between [1, 365]")
    if DepartureHour < 0 or DepartureHour > 23:
        raise ValueError("Departure hour must be between [0, 23]")
    
    def callback(cursor: mysql.cursor.MySQLCursor):
        query = f'INSERT INTO Flight ' \
                f'(FlightId, Departure, Destination, DepartureHour, DepartureDay, Duration, AvailableSeats)' \
                f'VALUES ({FlightId}, \'{Departure}\', \'{Destination}\', {DepartureHour}, {DepartureDay}, {Duration}, {NumberOfSeats})'
        cursor.execute(query)

    database_context(callback)


def RemoveFlight(FlightId: int):
    def callback(cursor: mysql.cursor.MySQLCursor):
        query = f'DELETE FROM Flight WHERE FlightId = {FlightId}'
        cursor.execute(query)
    
    database_context(callback)


def main():
    global DB_CONFIG
    DB_CONFIG = {
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'port': os.environ['DB_PORT'],
        'database': os.environ['DB_NAME']
    }

    while True:
        try:
            cmd = input("> ")
            tokens = cmd.split(" ")
            func = None
            if tokens[0] == AddFlight.__name__:
                func = AddFlight
            elif tokens[0] == RemoveFlight.__name__:
                func = RemoveFlight
            else:
                print(f"Command not recognized: {cmd}\nPossible commands:")
                print(POSSIBLE_ACTIONS)
                continue
            func(*tokens[1:])
        except (TypeError, mysql.Error, ValueError) as e:
            print(str(e))
        except (EOFError, KeyboardInterrupt):
            print()
            break

if __name__ == "__main__":
    main()