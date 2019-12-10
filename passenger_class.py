class Passenger(): # self = the instance of that object

    passenger_list_names = []
    passenger_list_number = []

    def __init__(self, full_name, passport_number):
        self.name = full_name
        self.passport_number = passport_number

    def add_passenger(self):
        while True:
            if len(self.name) > 2:
                passenger_list_names.append(self.name)
                passenger_list_number.append(self.passport_number)
                print(passenger_list_names)
                print('User added.')
            elif len(self.name) < 2:
                print('Invalid name please check and try again.')
            break



# Objects
passenger1 = Passenger('Joanna Thomson', 'B343123')
passenger2 = Passenger('Burt Kurman', 'B13927')
passenger3 = Passenger('', 'B90129')


#Lists
passenger_list_names = []
passenger_list_number = []

print(passenger1.add_passenger())
