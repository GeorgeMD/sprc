import os
import requests
from typing import List


POSSIBLE_ACTIONS = "GetRoute <Departure> <Destination> <MaxFlights> <DepartureDay>\nBookTicket <FlightIds>\nBuyTicket <ReservationId> <CreditCardInfo>"
SERVICE_URL = None


def BuildUrl(*params):
    return SERVICE_URL + "/".join([str(p) for p in params])


def GetRoute(Departure: str, Destination: str, MaxFlights: int, DepartureDay: int):
    DepartureDay = int(DepartureDay)
    if DepartureDay < 1 or DepartureDay > 365:
        raise ValueError("Departure day must be between [1, 365]")

    r = requests.get(BuildUrl('getOptimalRoute', Departure, Destination, MaxFlights, DepartureDay))
    response = r.json()
    if type(response) is str:
        print(response)
    else:
        print("\n".join(response['human_strings']))
        print(response["flightIds"])


def BookTicket(*FlightIds):
    r = requests.post(BuildUrl('bookTicket'), json={'flightIds': list(FlightIds)})
    try:
        reservationId = int(r.json())
        print(f"Reservation id: {reservationId}")
    except ValueError:
        print(r.json())


def BuyTicket(ReservationId, CreditCardInfo):
    r = requests.post(BuildUrl('buyTicket'), json={'reservationId': ReservationId, 'cardInfo': CreditCardInfo})
    print("\n".join(r.json()))


def main():
    global SERVICE_URL
    SERVICE_URL = os.environ['SERVICE_URL']

    while True:
        try:
            cmd = input("> ")
            tokens = cmd.split(" ")
            func = None
            if tokens[0] == GetRoute.__name__:
                func = GetRoute
            elif tokens[0] == BookTicket.__name__:
                func = BookTicket
            elif tokens[0] == BuyTicket.__name__:
                func = BuyTicket
                tokens = [tokens[0], tokens[1], " ".join(tokens[2:])]
            else:
                print(f"Command not recognized: {cmd}\nPossible commands:")
                print(POSSIBLE_ACTIONS)
                continue
            func(*tokens[1:])
        except (TypeError, ValueError) as e:
            print(str(e))
        except (EOFError, KeyboardInterrupt):
            print()
            break

if __name__ == "__main__":
    main()