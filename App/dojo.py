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
import click
import time

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
                click.secho(msg,bold=True, fg='yellow')
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

    def room_capacity(self):
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
            click.secho(msg.upper(),bold=True, fg='red')
            return msg
        else:
            click.secho('ADDING %s  ...' % (name.upper()), bold=True,fg='magenta')
            time.sleep(1)         
            print ("    ")
            room_names = [room.name for room in self.all_rooms] #gets room name of rooms added
            # adding a fellow with accomodation 
            if category == 'fellow':
                if wants_accomodation == 'Y':
                    new_person = Fellow(name)
                    if self.livingspace and self.office:
                        self.room_capacity()
                        if not self.dojo_lspace:
                            # if fellow is added with no allocation of a livingspace
                            self.unallocated.append(new_person)
                            msg = 'Livingspace %s has reached its maximum please add another room!'\
                            %(room.name.capitalize())
                            click.secho(msg,bold=True, fg='red')
                            return
                        if not self.dojo_office:
                            msg = 'The Office %s has reached its maximum please add another room!'\
                            %(room.name.capitalize())
                            click.secho(msg,bold=True, fg='red')
                            return
                        else:
                            # allocate an office and a livingspace to a person
                            # a random office and livingspace is generated
                            l_choice = random.choice(self.dojo_lspace)
                            #  Also, assign a fellow with accomodation a random office
                            o_choice = random.choice(self.dojo_office)
                            l_choice.members.append(new_person)
                            o_choice.members.append(new_person)
                            # add person to fellow list
                            self.fellows.append(new_person)
                            # add the person to all rooms
                            self.all_people.append(new_person)
                            msg = 'Fellow %s has been successfully added ! \n%s has been allocated to :\
                                    \nLivingspace: %s  |  Office: %s ' \
                                    %(new_person.name.capitalize(),new_person.name.capitalize(),\
                                    l_choice.name.capitalize(), o_choice.name.capitalize())
                            click.secho(msg,bold=False, fg='cyan')
                            print ("    ")
                    else:
                        msg = 'No Livingspaces found please add one with the create command.'
                        click.secho(msg,bold=True, fg='red')
                        print(' ')
                        return

                else:
                    # Adding a fellow who wants office space only
                    new_person = Fellow(name)
                    if self .office:
                        self.room_capacity()
                        if not self.dojo_office:     
                            msg = 'The Office %s has reached its maximum please add another room!'\
                            %(room.name.capitalize())
                            click.secho(msg,bold=True, fg='red')
                            return
                        else:
                            office_choice = random.choice(self.dojo_office)
                            ''' Adds user to room mebers list'''
                            office_choice.members.append(new_person)
                            # add person to fellow list
                            self.fellows.append(new_person)
                            # add the person to all people list
                            self.all_people.append(new_person)
                            msg = 'Fellow %s has been successfully added ! \n%s has been allocated to :\
                                        \nOffice: %s  |  Livingspace: None ' \
                                    %(new_person.name.capitalize(),new_person.name.capitalize(),\
                                    office_choice.name.capitalize())
                            click.secho(msg,bold=False, fg='cyan')
                            print ("    ")
                    else:
                        msg = 'No offices found please add one with the create command.'
                        click.secho(msg,bold=True, fg='red')
                        print ("    ")                    
            elif category == 'staff':
                print ("    ")
                new_person = Staff(name)
                if self.office:
                    self.room_capacity()
                    if not self.dojo_office:
                        msg = 'The Office %s has reached its maximum please add another room!'\
                        %(room.name.capitalize())
                        click.secho(msg,bold=True, fg='red')
                        return
                    else:
                        office_choice = random.choice(self.dojo_office)
                        new_person = Staff(name)
                        office_choice.members.append(new_person)
                        self.staff.append(new_person)
                        self.all_people.append(new_person)
                        msg = 'Staff %s has been successfully added ! \n%s has been allocated to :\
                                    \nOffice: %s  |  Livingspace: None ' \
                                %(new_person.name.capitalize(),new_person.name.capitalize(),\
                                office_choice.name.capitalize())
                        click.secho(msg,bold=False, fg='cyan')
                        print ("    ")
                else:
                    msg = 'No officesfound please add one with the create command.'
                    click.secho(msg,bold=True, fg='red')
                    print ("    ")
            else:
                # message if category is invalid
                print('Please enter either fellow or staff for adding person')
                print ("    ")
                return        

    def print_room(self, room_name):
        '''
        This function takes the name as an argument and pass it
        to print all the members in a room(name) if any
        '''
        click.secho('PRINTING ROOM %s  ...' % (room_name.upper()), bold=True,fg='magenta')
        time.sleep(1)          
        rooms = self.all_rooms
        if not rooms:
            click.secho('No rooms added yet!.', fg='red', bold=True)
            return 'No rooms exist at the moment.'
        for room in rooms:
            # checks for rooom name that is equal to the name argument given
            if room_name == room.name:
                print(" ")
                click.secho('=' * 30, fg='yellow')
                click.secho('%s ' %(room_name.capitalize()), fg='white', bold=True)
                click.secho('=' * 30, fg='yellow')
                if room.members:
                    # go through each and every member in a room
                    for member in room.members:
                        click.secho(member.name, fg='cyan')
                else:
                    # if a created room is empty with no members
                    click.secho('No members found :(.', fg='cyan', bold=True)
                click.secho('=' * 30, fg='yellow')
                print ("    ")
                return False
        else:
            # if no room is created 
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
        output = ''
        for room in rooms:
            output += '==' * 15
            output += '\n'
            output += room.name.upper()
            output += '\n'
            output += '==' * 15
            output += '\n'
            # go through all members added
            if room.members:
                for member in room.members:
                    output += member.name
                    output += '\n'
            else:
                # prints out a created room with no members
                output += 'There are no people  yet.'
                output += '\n'
        # This prints a list of all allocations onto the screen without the 
        # optional --o
        if filename == None:
            click.secho(output, fg='yellow')

        else:
            # prints the list of allocations to a specified file(.txt)
            click.secho('PLEASE WAIT...', bold=True, fg='magenta')
            time.sleep(1)
            print(' ')
            text = ''
            for room in rooms:
                text += room.name.upper() + "\n"
                text += "-" * 50 + "\n"
                if room.members:
                    text += " , " .join(member.name.capitalize() for member in room.members) + '\n'
                    text += '\n'
            # specify the fomart and mode
            file = open(filename + '.txt', 'w')
            file.write(text)
            click.secho('Your allocation list has been saved sucessfully \nas %s.txt'\
             % filename, bold=True, fg='green')
            return

    def print_unallocated(self, filename):
        unallocated = self.unallocated
        if not unallocated:
            click.secho('No rooms found in the Dojo', bold=True, fg='red')
            return        
        output = ''
        output += "=" * 20 + "\n"
        output += "Unallocated People\n"
        output += "=" * 20 + "\n"
        for person in unallocated:
            output += person.name + '\n'
        else:
            output += 'There are no people  yet.'
            output += '\n' 
        if filename == None:
            click.secho(output, fg='yellow')
        else:
            file = open(filename + 'txt', 'w')
            file.write(output)
            click.secho('Your allocation list has been saved sucessfully \nas %s.txt'\
            % filename, bold=True, fg='green')
            return