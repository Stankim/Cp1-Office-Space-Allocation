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
        self.allocated_people = []
        self.unallocated_people = []
        self.fellows = []
        self.allocated_fellows = []
        self.staff = []
        self.allocated_staff = []
        self.people = []

    
    def create_room(self, name, type_room):
        '''
        Create new rooms for person(s)
        '''
        if type_room.lower() in [type_room for room in self.all_rooms]:
            print("Sorry, Room already exists!!!")
            return " "
        else:        
            if type_room.lower() == 'livingspace':
                new_room = Livingspace(name)
                self.livingspace.append(new_room)
                self.all_rooms.append(new_room)
                msg = ' A Livingspace called %s has been successfully created!' % new_room.name
                print (msg)
            
            elif type_room.lower() == 'office':
                new_room = Office(name)
                self.office.append(new_room)
                self.all_rooms.append(new_room)
                msg = ' An office called %s has been successfully created!' % new_room.name
                print (msg)            
            else:
                print ('invalid')
        

    def check_vacant_rooms(self):
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
    

    def add_person(self, name, category, wants_accomodation= 'N'):
        """Add new person"""
        if category == 'fellow':
            person = Fellow(name)

            try:
                office_choice = random.choice(self.vacant_offices)
                self.check_vacant_rooms()
                if not self.vacant_offices:
                    print (' roo is not available')
                    return
            except IndexError:
                print ('nno rooms avail')
                return
            office_choice.members.append(person)
            # print('sucess')
            if wants_accomodation == 'Y':
                
                try:
                    livingspace_choice = random.choice(self.vacant_livingspaces)
                    if not self.vacant_livingspaces:
                        print ('room is not avail')
                        return
                except IndexError:
                    return  ('lspace not avail')
            self.fellows.append(person)
            self.all_people.append(person)
            print('success')
        elif category == 'staff':
            person = Staff(name)

            try:
                office_choice = random.choice(self.vacant_offices)
                self.check_vacant_rooms()
                if not self.vacant_offices:
                    print (' roo is not available')
                    return
            except IndexError:
                print ('nno rooms avail')
                return
            office_choice.members.append(person)
            self.staff.append(person)
            self.all_people.append(person)
        else:
            return ('inavalid')
            


            








                



