"""
File      : dojo.py
Date      : March, 2017
Author(s) : Jimmy Kimani <jimmykkimani@gmail.com>
Desc      : Office Allocator model module
"""
# ============================================================================
# necessary imports
# ============================================================================
import random
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
        self.vacant_rooms = []
        self.vacant_offices = []
        self.vacant_livingspaces = []
        self.allocated = []

    
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

    def check_vacant_room(self):
        ''' checks for vacant rooms and adds to list'''
        for office in self.office:
            if len(office.members) < office.capacity:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
            # removes full rooms from list
            elif len(office.members) >= office.capacity:
                if office in self.vacant_offices:
                    self.vacant_offices.remove(office)
                    self.vacant_rooms.remove(office)
            #  checks for vacant rooms in livingspace       
        for livingspace in self.livingspace:
            if len(livingspace.members) < livingspace.capacity:
                if livingspace not in self.vacant_livingspaces:
                    self.vacant_livingspaces.append(livingspace)
                    self.vacant_rooms.append(livingspace)
                elif len(livingspace.members) >= livingspace.capacity:
                    self.vacant_livingspaces.append(livingspace)
                    self.vacant_rooms.append(livingspace)
        
    def add_person(self, person_name, category, wants_accomodation='N'):
        ''' Add new person and allocates a room by random'''
        name = person_name
        # checks for accomodation 
        if wants_accomodation == 'N':
            if category == 'staff':
                person = Staff(name)
                self.staff.append(person)
            elif category == 'fellow':
                person = Fellow(name)
                self.fellows.append(person)
        else:
            if self.office:
                self.check_vacant_room()
                if not self.vacant_offices:
                    msg = 'There no vacant rooms '
                    print (msg)
                    return
                if category == 'staff':
                    office_select = random.choice(self.vacant_offices)
                    person = Staff(name)
                    # add members to list
                    office_select.members.append(person)
                    self.all_rooms.append(person)
                    msg = 'You have successfully allocated %s' % name 
                    print (msg)
                    print "  "
                    # adding a fellow to list
                elif category == 'fellow':
                    office_select = random.choice(self.vacant_offices)
                    person = Fellow(name)
                    office_select.members.append(person)
                    self.all_rooms.append(person)
                    msg = 'You have successfully allocated %s' % name 
                    print (msg)
                    print "  "
                self.all_rooms.append(person)
            else:
                print (' No offices found')
                return
# adding person to all people list
            self.all_people.append(person)
                    




                



