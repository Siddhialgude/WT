class City:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, source, destination, price, departure_time, arrival_time, Airline):
        self.source = source
        self.destination = destination
        self.price = price
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.Airline = Airline

class ExpertSystem:
    def __init__(self):
        self.cities = {}
        self.flights = []

    def add_city(self, name):
        city = City(name)
        self.cities[name] = city

    def add_flight(self, source, destination, price, departure_time, arrival_time, Airline):
        flight = Flight(source, destination, price, departure_time, arrival_time, Airline)
        self.flights.append(flight)

    def find_flights(self, source, destination):
        routes = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                routes.append(flight)
        return routes

    def suggest_route(self, source, destination, via_city):
        suggested_routes = []
        for flight in self.flights:
            if flight.source == source and flight.destination == via_city:
                via_flight = flight
                for second_flight in self.flights:
                    if second_flight.source == via_city and second_flight.destination == destination:
                        suggested_routes.append((via_flight, second_flight))
        return suggested_routes

    def search_flights(self, source, destination):
        direct_flights = self.find_flights(source, destination)
        if direct_flights:
            print("Direct flights from", source, "to", destination, ":")
            for flight in direct_flights:
                print("Departure:", flight.departure_time, "Arrival:", flight.arrival_time, "Price:", flight.price, "Airline: ",flight.Airline)
        else:
            print("No direct flights available from", source, "to", destination)
            for city in self.cities:
                if city != source and city != destination:
                    print("You can go from", source, "to", destination, "via", city)

    def ask_user(self):
        source = input("Enter the source city (type 'quit' to exit): ")
        print(" ")
        if source.lower() == 'quit':
            return
        destination = input("Enter the destination city: ")
        print(" ")
        self.search_flights(source, destination)
        self.ask_user()

# Example usage:
expert_system = ExpertSystem()

# Adding cities
expert_system.add_city("New York")
expert_system.add_city("Los Angeles")
expert_system.add_city("Chicago")
expert_system.add_city("Hawaii")


# Adding flights
expert_system.add_flight("New York", "Los Angeles", 3000, "08:00", "11:30","Delta")
expert_system.add_flight("New York", "Los Angeles", 2950, "17:00", "20:10", "Spirit")
expert_system.add_flight("New York", "Los Angeles", 2950, "1:00", "4:10", "United Airlines")
expert_system.add_flight("New York", "Chicago", 2500,"09:00", "11:00", "American Airlines")
expert_system.add_flight("New York", "Chicago", 2500,"12:00", "2:15", "Alaska Airlines")
expert_system.add_flight("Hawaii", "Los Angeles",6000, "12:00", "6:00", "United Airlines")
expert_system.add_flight("Hawaii", "Los Angeles",5500, "16:00", "22:00", "South West")
expert_system.add_flight("Chicago", "Hawaii", 9000, "15:00", "23:00","Delta")
expert_system.add_flight("Chicago", "Hawaii", 8000, "10:00", "18:11", "United Airlines")
expert_system.add_flight("Chicago", "Hawaii", 8500, "21:30", "5:30", "Alaska Airlines")
expert_system.add_flight("Hawaii", "New York", 8000, "10:00", "19:35", "South West")
expert_system.add_flight("Hawaii", "New York", 8000, "1:00", "10:35", "Spirit")
expert_system.add_flight("Hawaii", "New York", 8000, "17:00", "1:35", "Delta")
print(" ")

# Starting the expert system
expert_system.ask_user()


'''
OUTPUT:-
Enter the source city (type 'quit' to exit):  New York
 
Enter the destination city:  Los Angeles
 
Direct flights from New York to Los Angeles :
Departure: 08:00 Arrival: 11:30 Price: 3000 Airline:  Delta
Departure: 17:00 Arrival: 20:10 Price: 2950 Airline:  Spirit
Departure: 1:00 Arrival: 4:10 Price: 2950 Airline:  United Airlines

Enter the source city (type 'quit' to exit):  Hawaii
 
Enter the destination city:  Chicago
 
No direct flights available from Hawaii to Chicago
You can go from Hawaii to Chicago via New York
You can go from Hawaii to Chicago via Los Angeles

Enter the source city (type 'quit' to exit):  Chicago
 
Enter the destination city:  Hawaii
 
Direct flights from Chicago to Hawaii :
Departure: 15:00 Arrival: 23:00 Price: 9000 Airline:  Delta
Departure: 10:00 Arrival: 18:11 Price: 8000 Airline:  United Airlines
Departure: 21:30 Arrival: 5:30 Price: 8500 Airline:  Alaska Airlines

Enter the source city (type 'quit' to exit):  New York
 
Enter the destination city:  Chicago
 
Direct flights from New York to Chicago :
Departure: 09:00 Arrival: 11:00 Price: 2500 Airline:  American Airlines
Departure: 12:00 Arrival: 2:15 Price: 2500 Airline:  Alaska Airlines

Enter the source city (type 'quit' to exit):  quit'''