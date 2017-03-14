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
import time
import click

from  App.person import Fellow, Staff
from  App.rooms import Livingspace, Office

class Dojo(object):
    '''
    This is the main class that is used to import sub classes
    like Livngspace, Office, Staff, Fellow and instantiates
    them to perform specific instructions accordingly
    '''

    def __init__(self):
        self.all_rooms = []
        self.fellows = []
        self.staff = []
        self.office = []
        self.livingspace = []
        self.all_people = []
        self.available_rooms = []
        self.dojo_office = []
        self.dojo_lspace = []
        self.unallocated = []
    def create_room(self, name, type_room):
        '''
        The create_room function uses the arguments name and
        type_room and instantiates the rooms.
        '''
        print ('    ')
        room_names = [room.name for room in self.all_rooms]
        msg = ''
        if name in room_names:
            msg = "sorry, one or more room name's already exists!please choose another name"
            click.secho(msg,bold=True, fg='red')
            return msg
            print ('   ')
        else:
            '''Create new Livingspace for person(s)'''
            if type_room.lower() == 'livingspace':
                new_room = Livingspace(name)
                self.livingspace.append(new_room)
                self.all_rooms.append(new_room)
                msg = ' A Livingspace called %s has been successfully created!'\
                 % new_room.name.capitalize() 
                click.secho(msg, bold=True, fg='yellow')
                print ("    ")

            elif type_room.lower() == 'office':
                new_room = Office(name)
                self.office.append(new_room)
                self.all_rooms.append(new_room)
                msg = ' An office called %s has been successfully created!'\
                 % new_room.name.capitalize()
                click.secho(msg,bold=True, fg='yellow')
                print ("    ")
            else:
                print ('invalid')
                print("     ")

    def check_room_is_vacant(self):
        '''
        This function adds new rooms to a list where new members
        are allocated and later remove full ones from the list
        depending on the capacity value
        '''
        ofisi = self.office
        lspace = self.livingspace
        for office in ofisi:
            if len(office.members) < office.capacity:
                if office not in self.dojo_office:
                    self.dojo_office.append(office)
                    self.available_rooms.append(office)
            elif len(office.members) >= office.capacity:
                if office in self.dojo_office:
                    self.dojo_office.remove(office)
                    self.available_rooms.remove(office)
                    # checks vacant rooms and add to a list
        for livingspace in lspace:
            if len(livingspace.members) < livingspace.capacity:
                if livingspace not in self.dojo_lspace:
                    self.dojo_lspace.append(livingspace)
                    self.available_rooms.append(livingspace)     
            elif len(livingspace.members) >= livingspace.capacity:
                if livingspace in self.dojo_lspace:
                    self.dojo_lspace.remove(livingspace)
                    self.available_rooms.remove(livingspace)

    def add_person(self, name, category, wants_accomodation='N'):
        '''
        This function creates a person and allocates
        the person to a random room
        '''
        # validates input of duplicate names in the system
        all_names = [person.name for person in self.all_people]
        if name in all_names:
            msg="Sorry, %s already exists.please choose another name" %(person.name.capitalize())
            click.secho(msg.upper(), bold=True, fg='red')
            return msg
        else:
            click.secho('ADDING %s  ...' % (name.upper()), bold=True, fg='magenta')
            time.sleep(1)
            print ("    ")
            # adding a fellow with accomodation 
            if category == 'fellow':
                new_person = Fellow(name)
                self.fellows.append(new_person)
                # add the person to all rooms
                self.all_people.append(new_person)
                self.check_room_is_vacant()
                if not self.dojo_office and self.office is not None:
                    
                    self.unallocated.append(new_person)
                    msg = 'There are no offices or the offices are all full.'
                    click.secho(msg,bold=True, fg='red')
                else:
                    o_choice = random.choice(self.dojo_office)
                    o_choice.members.append(new_person)
                    msg = 'Fellow %s has been successfully added ! \n%s has been allocated to :\
                        \nOffice: %s ' \
                        %(new_person.name.capitalize(),new_person.name.capitalize(),\
                        o_choice.name.capitalize())
                    click.secho(msg,bold=False, fg='cyan')
                if wants_accomodation == 'Y':
                    self.check_room_is_vacant()
                    if not self.dojo_lspace:
                        self.unallocated.append(new_person)
                        msg = 'There are no Livingspace found or the Livingspaces are all full.'
                        click.secho(msg,bold=True, fg='red')
                    else:
                        click.secho('ALLOCATING LIVINGSPACE ...', fg='magenta')
                        time.sleep(1.1)
                        print ('    ')
                        l_choice = random.choice(self.dojo_lspace)
                        l_choice.members.append(new_person)
                        msg = 'Livingspace: %s' %(l_choice.name.capitalize())
                        click.secho(msg,bold=False, fg='cyan')

            elif category == 'staff':
                new_person = Staff(name)
                self.staff.append(new_person)
                # add the person to all rooms
                self.all_people.append(new_person)
                if self.office:
                    self.check_room_is_vacant()
                    if not self.dojo_office:
                        self.unallocated.append(new_person)
                        msg = 'One of the  Offices reached its maximum please add another office!'
                        click.secho(msg,bold=True, fg='red')
                    else:
                        o_choice = random.choice(self.dojo_office)
                        o_choice.members.append(new_person)
                        msg = 'Staff %s has been successfully added ! \n%s has been allocated to :\
                            \nOffice: %s ' \
                            %(new_person.name.capitalize(),new_person.name.capitalize(),\
                            o_choice.name.capitalize())
                        click.secho(msg,bold=False, fg='cyan')
                else:
                    self.unallocated.append(new_person)
                    msg = 'No offices found please add one with the create command.'
                    click.secho(msg,bold=True, fg='red')                        

    def print_room(self, room_name):
        '''
        This function takes the name as an argument and pass it
        to print all the members in a room(name) if any
        '''
        click.secho('PRINTING ROOM %s  ...' % (room_name.upper()), bold=True, fg='magenta')
        time.sleep(1) 
        rooms = self.all_rooms
        if not rooms:
            click.secho('No rooms added yet!.', fg='red', bold=True)
            return 'No rooms exist at the moment.'
        for room in rooms:
            # checks for rooom name that is equal to the name argument given
            if room_name == room.name:
                print(" ")
                click.secho('=' * 20, fg='yellow')
                click.secho('%s ' %(room_name.capitalize()), fg='white', bold=True)
                click.secho('=' * 20, fg='yellow')
                if room.members:
                    # go through each and every member in a room
                    for member in room.members:
                        click.secho(member.name.capitalize(), fg='cyan')
                else:
                    # if a created room is empty with no members
                    click.secho('No members found :(.', fg='cyan', bold=True)
                click.secho('=' * 20, fg='yellow')
                print ("    ")
                return False
        # if no room is added
        else:
            click.secho('Room %s seems not to exist would you like to add it?'\
            % (room_name.capitalize()), fg='red', bold=True)
            print ("    ")

    def print_allocations(self, filename):
        '''
        This function prints a list of members(allocated) of a
        specific room to the screen and to a file if opted
        '''
        # checks for rooms not added or created
        rooms = self.all_rooms
        if not rooms:
            click.secho('No rooms found in the Dojo', bold=True, fg='red')
            return
        click.secho('PRINTING ALLOCATIONS...', bold=True, fg='magenta')
        time.sleep(1)
        print(' ')
        output = ''
        for room in rooms:
            output += '=' * 25
            output += '\n'
            output += room.name.upper()
            output += '\n'
            output += '=' * 25
            output += '\n'
            # go through all members added
            if room.members:
                for member in room.members:
                    output += member.name.capitalize()
                    output += '\n'
            else:
                # prints out a created room with no members
                output += 'There are no people yet.'
                output += '\n'
        # This prints a list of all allocations onto the screen without the
        # optional --o
        if filename == None:
            click.secho(output, fg='blue')

        else:
            # prints the list of allocations to a specified file(.txt)
            click.secho('PLEASE WAIT...', bold=True, fg='magenta')
            time.sleep(1)
            print(' ')
            text = ''
            for room in rooms:
                text += room.name.upper() + "\n"
                text += "-" * 30 + "\n"
                if room.members:
                    text += " , " .join(member.name.capitalize() for member in room.members) + '\n'
                    text += '\n'
                else:
                    # prints out a created room with no members
                    text += 'There are no people yet.'
                    text += '\n'                    
            # specify the fomart and mode
            file = open(filename + '.txt', 'w')
            file.write(text)
            click.secho('Your allocation list has been saved sucessfully \nas %s.txt'\
             % filename, bold=True, fg='green')
            return

    def print_unallocated(self, filename):
        unallocated = self.unallocated
        output = ''
        output += "=" * 20 + "\n"
        output += "Unallocated People\n"
        output += "=" * 20 + "\n"
        for person in unallocated:
            output += person.name.capitalize() + '\n'
        if not unallocated:
            output += 'There are no people  yet.'
            output += '\n' 
        if filename == None:
            click.secho(output, fg='yellow')
        else:
            file = open(filename + '.txt', 'w')
            file.write(output)
            click.secho('Your allocation list has been saved sucessfully \nas %s.txt'\
            % filename, bold=True, fg='green')
            return
    def reallocate_person(self, person_name, new_room_name):
        # This goes through the list of all people
        all_names = [person.name for person in self.all_people]
        for name in all_names:
            # checks if the name of the person exists
            if name == 'person_name':
                if person_name in all_names:
                    room_type = self.check_room_is_vacant()
                
            
        

    def load_people(self, filename):
        pass
