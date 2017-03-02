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

