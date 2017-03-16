import unittest
import os
from App.dojo import Dojo

class TestDojo(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()


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