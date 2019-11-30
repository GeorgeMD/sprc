CREATE DATABASE IF NOT EXISTS AirplaneService;
use AirplaneService;

CREATE TABLE IF NOT EXISTS Flight(
    FlightId INT NOT NULL,
    Departure VARCHAR(100) NOT NULL,
    Destination VARCHAR(100) NOT NULL,
    DepartureHour INT NOT NULL,
    DepartureDay INT NOT NULL,
    Duration INT NOT NULL,
    AvailableSeats INT NOT NULL,
    BookedSeats INT NOT NULL DEFAULT 0,
    BoughtSeats INT NOT NULL DEFAULT 0,
    PRIMARY KEY (FlightId)
);

CREATE TABLE IF NOT EXISTS Reservation(
    ReservationId INT NOT NULL AUTO_INCREMENT,
    WasBought BOOLEAN NOT NULL DEFAULT false,
    PRIMARY KEY (ReservationId)
);

CREATE TABLE IF NOT EXISTS ReservationFlight(
    ReservationId INT NOT NULL,
    FlightId INT NOT NULL,
    PRIMARY KEY (ReservationId, FlightId),
    FOREIGN KEY (ReservationId) REFERENCES Reservation(ReservationId),
    FOREIGN KEY (FlightId) REFERENCES Flight(FlightId)
);