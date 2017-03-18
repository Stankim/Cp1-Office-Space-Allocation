
"""
File      : dojo.py
Date      : March, 2017
Client    : Andela 21
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
from  db.models import Persons, Rooms, create_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text, select
import os.path


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
        self.vacant_rooms = []
        self.vacant_offices = []
        self.vacant_livingspace = []
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
            if type_room == 'livingspace':
                room_type = 'LivingSpace'
                new_room = Livingspace(name)
                self.livingspace.append(new_room)
                self.all_rooms.append(new_room)
                msg = ' A Livingspace called %s has been successfully created!'\
                 % new_room.name.capitalize() 
                click.secho(msg, bold=True, fg='yellow')
                print ("    ")

            elif type_room == 'office':
                room_type = 'Office'
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
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
            elif len(office.members) >= office.capacity:
                if office in self.vacant_offices:
                    self.vacant_offices.remove(office)
                    self.vacant_rooms.remove(office)
                    # checks vacant rooms and add to a list
        for livingspace in lspace:
            if len(livingspace.members) < livingspace.capacity:
                if livingspace not in self.vacant_livingspace:
                    self.vacant_livingspace.append(livingspace)
                    self.vacant_rooms.append(livingspace)     
            elif len(livingspace.members) >= livingspace.capacity:
                if livingspace in self.vacant_livingspace:
                    self.vacant_livingspace.remove(livingspace)
                    self.vacant_rooms.remove(livingspace)

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
                if self.office or self.livingspace:
                    if not self.vacant_offices:
                        self.unallocated.append(new_person)
                        msg = 'There are no offices or the offices are all full.'
                        click.secho(msg,bold=True, fg='red')
                    else:
                        randomized_office = random.choice(self.vacant_offices)
                        # assign an office to fellow
                        new_person.office= randomized_office
                        # populate members list with new person(s)
                        randomized_office.members.append(new_person)

                        msg = 'Fellow %s has been successfully added ! \n%s has been allocated to :\
                            \nOffice: %s ' \
                            %(new_person.name.capitalize(),new_person.name.capitalize(),\
                            randomized_office.name.capitalize())
                        click.secho(msg,bold=False, fg='cyan')
                    if wants_accomodation == 'Y':
                        self.check_room_is_vacant()
                        if not self.vacant_livingspace:
                            self.unallocated.append(new_person)
                            msg = 'There are no Livingspace found or the Livingspaces are all full.'
                            click.secho(msg,bold=True, fg='red')
                        else:
                            click.secho('ALLOCATING LIVINGSPACE ...', fg='magenta')
                            time.sleep(1.1)
                            print ('    ')
                            randomized_lspace = random.choice(self.vacant_livingspace)
                            new_person.livingspace = randomized_lspace
                            randomized_lspace.members.append(new_person)
                            msg = 'Livingspace: %s' %(randomized_lspace.name.capitalize())
                            click.secho(msg,bold=False, fg='cyan')
                else:
                    self.unallocated.append(new_person)
                    click.secho('No Rooms found please add one with the create command.',bold=True, fg='red')
                            

            elif category == 'staff':
                new_person = Staff(name)
                self.staff.append(new_person)
                # add the person to all rooms
                self.all_people.append(new_person)
                if self.office:
                    self.check_room_is_vacant()
                    if not self.vacant_offices:
                        self.unallocated.append(new_person)
                        msg = 'One of the  Offices reached its maximum please add another office!'
                        click.secho(msg,bold=True, fg='red')
                    else:
                        randomized_office = random.choice(self.vacant_offices)
                        new_person.office= randomized_office
                        randomized_office.members.append(new_person)
                        msg = 'Staff %s has been successfully added ! \n%s has been allocated to :\
                            \nOffice: %s ' \
                            %(new_person.name.capitalize(),new_person.name.capitalize(),\
                            randomized_office.name.capitalize())
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
            output += room.name.upper() + "  "'|' ' '+ room.room_type
            output += '\n'
            output += '=' * 25
            output += '\n'
            # go through all members added
            if room.members:
                for member in room.members:
                    output += member.name.capitalize()+ " "'(' + member.person_type+ ')'
                    output += '\n'
            else:
                # prints out a created room with no members
                output += 'There are no people yet.'
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

    def reallocate_person(self, name, new_room_name):
        '''
        This function reallocates a person to another
        room be it an office or a fellow to a livingspace
        '''
        rooms = self.all_rooms
        new_person = None
        # go through the list of all people and check if person exist
        for people in self.all_people:
            if people.name == name:
                new_person = people
        # if person to reallocate is not in the system
        if new_person is None:
            click.secho('The person name entered does not exist.' ,bold=True, fg='red')
            return
        # go through a list of all rooms
        for room in rooms:
            if room.name == new_room_name:
                # assign new variable
                new_room = room
        # check if the room entered is in the system and vacant
        if new_room_name not in [room.name for room in self.all_rooms]:
            click.secho('The room %s does not exist.'%(new_room_name),bold=True, fg='red')
            return
        if new_person.wants_accomodation == 'N' and new_room in self.livingspace:
                click.secho("without accomodation you can't be allocated livingspaces." ,bold=True, fg='red')
                return
        # lets not add a staff to a livingspace
        # check new_person in staff list
        if new_person in self.staff and new_room in self.livingspace:
                click.secho("Staff members can't be allocated livingspaces." ,bold=True, fg='red')
                return
        # checks if person added actually has been alloacted a room
        for room in self.vacant_rooms:
            if new_person.name in [person.name for person in room.members]:
                if new_room == room:
                    # lets not allocate new_person to the same room
                    click.secho('The person is already a member of room %s.' %(new_room.name),bold=True, fg='red')
                    return
                else:
                    # remove person from the current room 
                    room.members.remove(new_person)
        # add new_person to  new room
        new_room.members.append(new_person)
        # add person to all_people list
        self.all_people.append(new_person)
        # if person is fellow add to fellows list
        if new_person == 'Fellow':
            self.fellows.append(new_person)
        else:
            self.staff.append(new_person)
        click.secho('%s has been reallocated to %s' %(new_person.name, new_room.name),bold=True, fg='green')
        # reallocate members who dont have allocations to vacant rooms
        if new_person in self.unallocated:
            self.unallocated.remove(new_person)

                    
    def load_people(self, filename):
        '''
        This function loads people from a text
        file and populated the system with members
        '''
        if filename:
            with open(filename + '.txt', 'r') as file:
                # read the file content by line and go through the list
                # of the file format
                for line in file:
                    data = line.split()
                    first_name = data[0]
                    second_name = data[1]
                    name = first_name + ' ' + second_name
                    category = data[2].lower()
                    # look for person with accomodation option
                    if len(data) == 4 :
                        wants_accomodation = data [3]
                    # incase there none default "N"
                    else:
                        wants_accomodation = 'N'
                    self.add_person(name.lower(), category,wants_accomodation)
                    click.secho('Success',fg='green')
        else:
            print('please provide a file')
                 
    def save_state(self,db_name='dojo'):
        '''
        Persists all the data stored in the app to a 
        SQLite database. Specifying the --db parameter
        explicitly stores the data in the sqlite_database 
        specified. 
        '''
        # create engine
        engine = create_db(db_name)
        # connect to db
        Base.metadata.bind = engine
        Session = sessionmaker()
        session = Session()

        # function to select all rooms in the Rooms table
        items = select([Rooms])
        res = session.execute(items)
        db_room_list =[item.room.name for item in res]

        for room in self.all_rooms:
            if room.name not in db_room_list:
                new_room = Rooms(name=room.name,
                                type_room = room.room_type,room_capacity = room.capacity)
                session.add(new_room)
                session.commit()

        people = select([Persons])
        response = session.execute(people)
        dbpersons_list = [item.person.name for item in response]
        # go through all people in all people list
        for person in self.all_people:
            if person.name not in dbpersons_list:
                # get the neccessary office names from objects
                if person.office is None:
                    # If fellow or staff have no offices allocated
                    people.office = 'has no office'
                else:
                  office_allocated = person.office.name
                #    If fellows have no livingspaces allocated
                if person.livingspace is None:
                    livingspace_allocated = "no room"
                else:
                  livingspace_allocated= person.livingspace.name
                accomodation = person.wants_accomodation
                new_p = Persons(
                    name=person.name,
                    category=person.person_type,
                    wants_accomodation= accomodation,
                    office_allocated= office_allocated,
                    living_space_allocated= livingspace_allocated)
                # add new person to db
                session.add(new_p)
                session.commit()
                message = "Data added to {} database successfully"
                click.secho(message, fg='green', bold=True)   

    def load_state(self, db_name):
        '''
         This function loads data from a database into the application.
        '''
        if not os.path.isfile(db_name):
            print("Database does not exist")
        else:    
            # create engine
            engine = create_engine('sqlite:///' + db_name)
            # Bind engine to Base Metadata
            Base.metadata.bind = engine
            # creates session
            Session = sessionmaker(bind=engine)
            session = Session()
            # Rooms --->
            # gets all the rooms in Rooms
            items = select([Rooms])
            # create an instance of the Rooms class where data is loaded
            res = session.execute(items)
            # queries all the result to enable tabulation of data
            for item in res.fetchall():
                # assign new variables
                r_name = item.name
                r_type = item.type_room

                if r_type == 'Office':
                    # check if there are no rooms in the sysytem and create one
                    if len(self.vacant_offices) == 0:
                        # pass room name and room type from db as arguments to create a new room
                        self.create_room(r_name, r_type.lower())
                    else:
                        for room in self.office:
                            if not self.vacant_offices:
                                self.create_room(r_name, r_type.lower())
                else:
                    if len(self.vacant_livingspace) == 0:
                         self.create_room(r_name, r_type.lower())
                    else:
                        for room in self.livingspace:
                            if not self.vacant_livingspace:
                                 self.create_room(r_name, r_type.lower())
            session.close()
            # Persons --->
            # get all the persons(s) in Persons
            items = select([Persons])
            result = session.execute(items)
            # query all results
            for item in result.fetchall():
                data = item.name.split()
                first_name = data[0]
                second_name = data[1]
                role = item.category
                person = first_name + ' ' + second_name 
                office_allocated = item.office_allocated
                livingspace_allocated = item.living_space_allocated

                if role == 'Staff':
                    new_person = Staff(person)
                    for room in self.all_rooms:
                         # check if room is == rooms created
                        # Populate the allocations variable with appropriate data from db
                        if office_allocated == room.name:
                            # along with members
                            room.members.append(new_person)
                            break
                elif role == 'Fellow':
                    new_person= Fellow(person)
                    for room in self.all_rooms:
                        # populate dojo rooms with all offices in the db
                        if office_allocated == room.name:
                            # as well as members allocations
                            room.members.append(new_person)
                            break
                    for room in self.livingspace:
                        if room.name == livingspace_allocated:
                            room.members.append(new_person)
                if role == 'Staff':
                    person_obj = Staff(person)
                    self.staff.append(person_obj)
                    self.all_people.append(person_obj)
                elif role == 'Fellow':
                    person_obj = Fellow(person)
                    self.fellows.append(person_obj)
                    self.all_people.append(person_obj)
            print('Load successful!')    

        

                    
