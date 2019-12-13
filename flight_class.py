class Flight():
    def __init__(self, plane_number=None ,origin=None, destination=None):
        self.origin = origin
        self.flight_number = plane_number
        self.destination = destination
        self.passenger_list = []

    # def add_plane(self):
    #     new_plane = Flight()
    #     plane_list.append(new_plane1)
    #     return 'Plane Has been Added'

# Objects
flight1 = Flight('Florida', 'BA1234')

# Lists
plane_list = []


# print(flight1.add_plane())
# print(plane_list)

plane_list.append(flight1.origin)
print(plane_list)
