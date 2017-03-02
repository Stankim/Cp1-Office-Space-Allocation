import unittest
from App.dojo import Dojo

class TestDojo(unittest.TestCase):
    '''
    Test Fixture: a piece of code that can construct and configure
    the system and the tasks getting ready to be tested and then cleans up
    '''
    def setUp(self):
        self.dojo = Dojo()


    def test_create_room_successfully(self):
        
        self.assertEqual(len(self.dojo.all_rooms), 0)
        self.dojo.create_room('Blue', 'office')
        self.assertEqual(len(self.dojo.all_rooms), 1, 'rooms added successfully')

    def test_create_multiple_offices(self):
        self.assertEqual(len(self.dojo.all_rooms), 0)
        self.dojo.create_room('Blue', 'office')
        self.dojo.create_room('Black', 'office')
        self.dojo.create_room('Brown', 'office')
        self.assertEqual(len(self.dojo.all_rooms), 3, 'rooms added successfully')

    def test_office_is_created(self):
        '''test to confirm an office is created'''
        office = self.dojo.office
        self.assertEqual(len(office), 0)
        self.dojo.create_room('green', 'office')
        self.assertEqual(len(office), 1)
        
    def test_living_space_is_created(self):
        '''test to confirm that living space is created'''
        livingspace = self.dojo.livingspace
        self.assertEqual(len(livingspace), 0)
        self.dojo.create_room('crypton', 'livingspace')
        self.assertEqual(len(livingspace), 1)
        
    
    def test_add_person_added_successfully(self):
        '''
        tests that all person(s) are added
        '''
        self.assertEqual(len(self.dojo.all_people), 0)
        self.dojo.create_room('brown', 'office')
        self.dojo.create_room('red', 'livingspace')
        self.dojo.add_person('kobby','fellow', 'y')
        self.dojo.add_person('bett', 'staff')
        self.assertEqual(len(self.dojo.all_people), 2)

    def test_fellow_is_added_successfully(self):
        '''
        test to confirm a fellow is added
        '''
        self.dojo.create_room('brown', 'office')
        self.assertEqual(len(self.dojo.fellows), 0)
        self.dojo.add_person('khalid', 'fellow', 'y')
        self.assertEqual(len(self.dojo.all_people), 1 , 'fellow successfully added')

    def test_staff_is_added_sucessfully(self):
        '''
        tests to confirm staff is added
        '''
        self.dojo.create_room('blue', 'office')
        self.assertEqual(len(self.dojo.staff), 0)
        self.dojo.add_person('sonia', 'staff')
        self.assertEqual(len(self.dojo.all_people), 1, 'staff sucessfully added')

    def test_person_is_allocated_a_room(self):
        '''test if a person has been reallocated to a room'''
        self.dojo.create_room('yellow', 'office')
        self.dojo.add_person('pink', 'fellow')
        person = self.dojo.fellows[0]
        room_name = person.office.name
        self.assertEqual(room_name, 'pink')