"""
File      : dojo.py
Date      : March, 2017
Author(s) : Jimmy Kimani <jimmykkimani@gmail.com>
Desc      : Office Allocator model module
"""
# ============================================================================
# necessary imports
# ============================================================================
from rooms import Livingspace, Office
from person import Fellow, Staff

class Dojo(object):
    
    def __init__(self):
        self.all_rooms = []
        self.fellows = []
        self.staff = []
        self.all_people = []
        self.livingspace = []
        self.office = []

    
    def create_room(self, name, type_room):
        '''
        Create new rooms for person(s)
        '''
        if type_room.lower() == 'livingspace':
            new_room = Livingspace(name)
            self.livingspace.append(new_room)
            self.all_rooms.append(new_room)
            msg = ' %s added successfully' % new_room
            print (msg)
        
        elif type_room.lower() == 'office':
            new_room = Office(name)
            self.office.append(new_room)
            self.all_rooms.append(new_room)
            msg = ' %s added successfully' % new_room
            print (msg)            
        else:
            return 'Invalid'


    def add_person(self, person_name, category, wants_accomodation = 'N'):
        
        '''
        Adds person(person name), category(Fellow/Staff)
        '''


