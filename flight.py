class Flight:
    def __init__(self, flight_number, destination, origin, total_seats):
        self.flight_number = flight_number
        self.destination = destination
        self.origin = origin
        self.total_seats = total_seats
        self.booked_seats = 0
        self.passenger_list = []

    def book_seat(self, passenger_name):
        if self.booked_seats >= self.total_seats:
            raise ValueError("Flight is fully booked")
        self.passenger_list.append(passenger_name)
        self.booked_seats += 1

    def cancel_booking(self, passenger_name):
        if passenger_name not in self.passenger_list:
            raise ValueError("Passenger not found")
        self.passenger_list.remove(passenger_name)
        self.booked_seats -= 1

    def available_seats(self):
        return self.total_seats - self.booked_seats


class Customer:
    def __init__(self, name):
        self.name = name
        self.bookings = []

    def book_flight(self, flight, passenger_name=None):
        if passenger_name is None:
            passenger_name = self.name
        flight.book_seat(passenger_name)
        self.bookings.append(flight)

    def cancel_flight(self, flight, passenger_name=None):
        if passenger_name is None:
            passenger_name = self.name
        flight.cancel_booking(passenger_name)
        self.bookings.remove(flight)
