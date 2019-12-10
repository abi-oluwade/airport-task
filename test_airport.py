from passenger_class import *
from flight_class import *
import pytest

#Tests divided into SETUP and ASSERTIONS

def test_create_passenger():
    # SETUP
    #specify objects here# then assert the objectd.attribute
    #ASSERTION
    assert Passenger('Joanna Thomson', 'B343123').name == 'Joanna Thomson'
    assert passenger1.name == 'Joanna Thomson'
    assert passenger1.passport_number == 'B343123'

def test_create_joana_thomson():
    passenger_test1 = Passenger('Joanna Thomson', 'B343123')
    assert passenger_test1.name == 'Joanna Thomson' and passenger_test1.passport_number == 'B343123'

def test_create_burt_kurman():
    passenger_test2 = Passenger('Burt Kurman', 'B13927')
    assert passenger_test2.name == 'Burt Kurman' and passenger_test2.passport_number == 'B13927'

def test_no_name_or_passport():
    try:
        with pytest.raises(TypeError):
                Passenger()
    finally: 'Invalid Input'

def test_create_flight():
    new_plane = Flight('1234')
    assert new_plane.flight_number == ('1234')

def add_plane():
    new_plane = Flight('1234')
    assert new_plane.flight_number == ['1234']

def add_destination():
    new_plane = Flight('1234','New York', 'London')
    assert new_plane.destination == 'London'

def add_origin():
    new_plane = Flight('1234', 'France', 'Miami')
    assert new_plane.origin == 'France'

def add_passenger_to_list():
    passenger_list = []
    passenger4 = Passenger('Jason Bourne','1001')
    passenger_list.append(passenger4.name)
    assert passenger_list.append(passenger4.name) == 'Jason Bourne'