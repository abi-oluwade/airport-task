class Flight():

    flight_list = ['Florida', 'Germany','New York']

    def __init__(self, destination=None, plane_number=None, origin=None):
        self.origin = origin
        self.flight_number = plane_number
        self.destination = destination

    # def add_plane(self):
    #     new_plane = Flight()
    #     plane_list.append(new_plane1)
    #     return 'Plane Has been Added'

    def list_flights(self):
        for flights in flight_list:
            print(flights)


# Objects
flight1 = Flight('Florida', 'BA1234')
flight2 = Flight('Germany', 'BA5678')
flight3 = Flight('New York', 'BA9101')

# Lists
flight_list = []


# print(Flight.list_flights(flight1))
