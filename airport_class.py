class Passenger(): # self = the instance of that object
    def __init__(self, full_name, passport_number):
        self.name = full_name
        self.passport_number = passport_number

passenger1 = Passenger('Joanna Thomson', 'B343123')
passenger2 = Passenger('Burt Kurman', 'B13927')
passenger3 = Passenger('', 'B90129')

