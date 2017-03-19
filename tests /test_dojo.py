import unittest
import os
from App.dojo import Dojo

class TestDojo(unittest.TestCase):
    '''
    Test Fixture: a piece of code that can construct and configure
    the system and the tasks getting ready to be tested and then cleans up
    '''
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.office = []
        self.dojo.available_rooms = []


    def test_create_room_successfully(self):
        
        self.assertEqual(len(self.dojo.all_rooms), 0)
        self.dojo.create_room('Blue', 'office')
        self.assertEqual(len(self.dojo.all_rooms), 1, 'rooms added successfully')

    def test_create_multiple_offices(self):
        self.assertEqual(len(self.dojo.all_rooms), 0)
        self.dojo.create_room('Blue', 'office')
        self.dojo.create_room('Black', 'office')
        self.dojo.create_room('Brown', 'office')
        self.assertEqual(len(self.dojo.all_rooms), 3)

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
        tests that all person(s) are added succesfully 
        '''
        self.assertEqual(len(self.dojo.all_rooms), 0)
        self.dojo.create_room('brown', 'office')
        self.dojo.create_room('red', 'livingspace')
        self.dojo.add_person('kobby', 'Staff')
        self.dojo.add_person('bett', 'Fellow')

    def test_add_person_with_no_room(self):
        '''
        tests that all person(s) are added
        '''
        self.assertEqual(len(self.dojo.all_rooms), 0)
        self.dojo.create_room('', 'office')
        self.dojo.create_room('', 'livingspace')
        self.dojo.add_person('kobby', 'Staff')
        self.dojo.add_person('bett', 'Fellow')
        self.assertEqual(len(self.dojo.all_rooms), 1)        

    def test_fellow_is_added_successfully(self):
        '''
        test to confirm a fellow is added
        '''
        self.dojo.create_room('brown', 'office')
        self.assertEqual(len(self.dojo.fellows), 0)
        self.dojo.add_person('khalid', 'Fellow', 'Y')
        self.assertEqual(len(self.dojo.all_rooms), 1, 'fellow successfully added')

    def test_fellow_accomodation_is_added_successfully(self):
        '''
        test to confirm a fellow is added
        '''
        self.dojo.create_room('brown', 'livingspace')
        self.assertEqual(len(self.dojo.fellows), 0)
        self.dojo.add_person('khalid', 'Fellow', 'Y')
        self.assertEqual(len(self.dojo.all_rooms), 1, 'fellow successfully added')        

    def test_staff_is_added_sucessfully(self):
        '''
        test to confirm staff is added
        '''
        self.dojo.create_room('blue', 'office')
        self.assertEqual(len(self.dojo.staff), 0)
        self.dojo.add_person('kobby', 'Staff', 'N')
        self.assertEqual(len(self.dojo.all_rooms), 1, 'staff sucessfully added')

    def test_room_with_same_name_not_created(self):
        self.dojo.create_room("blue", "office")
        r_names = [r.name for r in self.dojo.all_rooms]
        self.assertIn("blue", r_names)
        msg = self.dojo.create_room("blue", "office")
        self.assertEqual(msg, "sorry, one or more room name's already exists!please choose another name") 

    def test_vacant_rooms_added_successfully(self):
        self.assertEqual(len(self.dojo.all_rooms), 0)      
        self.dojo.create_room('blue', 'livingspace')
        self.dojo.create_room('red', 'office')
        self.dojo.add_person('kobby', 'staff')
        self.dojo.add_person('bett', 'fellow')        
        self.assertEqual(len(self.dojo.dojo_lspace), 1)
        self.assertEqual(len(self.dojo.dojo_office), 1) 
        
    def test_print_room(self):
        '''test that members of a room are printed'''
        self.dojo.create_room('blue', 'office')
        self.dojo.create_room('brown', 'livingspace')
        self.dojo.add_person('sonia', 'fellow')
        self.dojo.add_person('kobby', 'staff')
        self.dojo.add_person('bett', 'fellow')
        self.dojo.print_room('blue')

    def test_print_room_not_added(self):
        '''test that members of a room are created'''
        self.dojo.create_room('', 'office')
        self.dojo.create_room('', 'livingspace')
        self.dojo.add_person('sonia', 'fellow')
        self.dojo.add_person('kobby', 'staff')
        self.dojo.add_person('bett', 'fellow')
        self.dojo.print_room('blue')

    def test_invalid_print_room(self):
        '''test invalid room '''
        self.dojo.create_room('blue', 'office')
        self.dojo.create_room('brown', 'livingspace')
        self.dojo.add_person('sonia', 'fellow' 'Y')
        self.dojo.add_person('kobby', 'staff')
        self.dojo.add_person('bett', 'fellow')
        self.dojo.print_room('green')

    def test_print_allocations_filename(self):
        '''test that allocated people are printed to a file'''
        self.dojo.create_room('BLUE', 'office')
        self.dojo.add_person('kobby', 'staff')
        self.dojo.print_allocations('allocated')
        self.assertTrue(os.path.isfile('allocated.txt')) 
        file = open('allocated.txt', 'r')
        output = file.readlines()
        first_line = output [0]
        second_line = output [2]
        self.assertEquals(first_line, 'BLUE' + "\n")
        self.assertEquals(second_line, 'Kobby' + "\n")

    def test_print_unallocated_filename(self):
        '''test that unallocated people are printed to a file'''
        self.dojo.add_person('kobby', 'fellow','Y')
        self.dojo.print_unallocated('unallocated') 
        self.assertTrue(os.path.isfile('unallocated.txt'))
        unallocated_file = open('unallocated.txt', 'r')
        text = unallocated_file.readlines()
        first_line = text [0]
        second_line = text [1]
        third_line = text[3]
        self.assertEquals(first_line, "=" * 20 + "\n")
        self.assertEquals(second_line, 'Unallocated People' + "\n")
        self.assertEquals(third_line, "Kobby" + '\n') 

    #    tests for reallocate person starts here --->
    def test_reallocate_person(self):
        self.dojo.create_room('hogwarts','office')
        self.dojo.create_room('swift', 'livingspace')
        self.dojo.add_person("john", "fellow")
        res = self.dojo.reallocate_person('john', 'swift')
        self.assertEqual(res,None)

    def test_reallocate_person_if_person_name_is_invalid(self):
        self.dojo.create_room('hogwarts','office')
        self.dojo.create_room('swift', 'livingspace')
        self.dojo.add_person("john", "fellow")
        res = self.dojo.reallocate_person('joe', 'swift')
        self.assertEqual(res,None) 

    def test_reallocate_person_to_livingspace_if_person_is_staff(self):
        self.dojo.create_room('hogwarts','office')
        self.dojo.create_room('swift', 'livingspace')
        self.dojo.add_person("kimani", "staff")
        res = self.dojo.reallocate_person('kimani', 'swift')
        self.assertEqual(res,None)        

    def test_reallocate_to_same_room(self):
        self.dojo.create_room('hogwarts','office')
        self.dojo.create_room('swift', 'livingspace')
        self.dojo.add_person("john", "fellow")
        res = self.dojo.reallocate_person('joe', 'hogwarts')
        self.assertEqual(res,None)  

    def test_a_person_has_been_removed_from_a_room_after_reallocation(self):
        self.dojo.create_room('hogwarts', 'office')
        self.dojo.add_person('wick', 'fellow')
        office = self.dojo.dojo_office[0]
        members = office.members
        self.assertEqual(len(members), 1)
        self.dojo.create_room('php', 'office')
        self.dojo.reallocate_person('wick', 'php')
        office = self.dojo.dojo_office[0]
        members = office.members
        self.assertEqual(len(members), 1)

    def test_if_a_room_doesnt_exist(self):
        self.dojo.create_room('hogwarts','office')
        self.dojo.create_room('swift', 'livingspace')
        self.dojo.add_person("john", "fellow")
        res = self.dojo.reallocate_person('joe', 'hogwarts3')
        self.assertEqual(res,None) 

        # test for load people from file --->
    def test_load_people(self):
        self.dojo.create_room('hogwarts', 'office')
        self.dojo.create_room('swift', 'livingspace')
        staff = self.dojo.staff
        fellows = self.dojo.fellows
        self.assertEqual(len(staff), 0)
        self.assertEqual(len(fellows), 0)
        self.dojo.load_people("sample")
        self.assertEqual(len(staff), 3)
        self.assertEqual(len(fellows), 4)

    def test_it_saves_state(self):
        self.dojo.save_state('testdb')
        self.assertFalse (os.path.isfile ('testdb.sqlite'))

    def save_state_works(self):
        """Test that application data can be saved to user-defined database"""
        self.dojo.create_room('hogwarts', 'office')
        self.dojo.add_person('wick', 'fellow')
        person = self.dojo.add_person("kimani", "fellow", "Y")
        res = self.dojo.save_state('testdb')
        self.assertEqual(res, True)