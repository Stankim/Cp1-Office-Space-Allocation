#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    dojo (-i | --interactive)
    dojo (-h | --help | --version)
    dojo create_room <room_name> (livingspace|Office)...
    dojo add_person <fname> <lname> (fellow|staff) [<accommodation>]
    dojo print_room <room_name>

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
import click
from docopt import docopt, DocoptExit
from App.dojo import Dojo
from App.person import Fellow, Staff
from intro import intro_dojo
from pyfiglet import figlet_format
from termcolor import cprint , colored
dojo = Dojo()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def start():
    intro_dojo()


class Interactive (cmd.Cmd):
   

    dojo_prompt = colored('The Dojo > ', 'magenta', attrs=['bold'])
    prompt = dojo_prompt
    

    @docopt_cmd
    def do_create_room(self, arg):
        """
        This command creates rooms in The Dojo.

        You can create  rooms by specifying room names
        after the create_room command. By default, this method will create an
        Office/Livingspace into the system.

        Usage: create_room <room_name> <room_type>
        """
        name = arg['<room_name>']
        type_room  = arg['<room_type>']

        create_room_status = dojo.create_room(name, type_room)
        if create_room_status == 'Invalid':
            print(create_room_status)
            return
        # print (dojo.all_rooms)

        
    @docopt_cmd
    def do_add_person(self, arg):
        """
        This command adds a person and allocates them a random room in The Dojo

        The <role> argument specifies the role of the person being added
        which can either be 'Fellow' or 'Staff'.

        The <wants_accommodation> Here is an option argument which can
        be either Y or N. The default value if not provided is N

        Usage: add_person <first_name> <last_name> <role> [<accomodation>]
        """
        name = arg['<first_name>'] + " " + arg["<last_name>"]
        role = arg['<role>']
        wants_accomodation = arg['<accomodation>']

        dojo.add_person(name, role, wants_accomodation)

    @docopt_cmd
    def do_print_room(self, arg):
        """
        This commands prints room details.

        It accepts a room name then querries System and returns
        information about the room given.

        Usage: print_room <room_name>
        """
        room_name = arg['<room_name>']

        dojo.print_room(room_name)


    @docopt_cmd
    def do_print_allocations(self, arg):
        """
        This commands prints a list of allocations to the screen specifying
        the optional --o 

        It simply takes the name of the file to save the allocations printout
        If not provided, the printout will not be saved to a file.

        All allocations files are saved in the root directory.

        Usage: print_allocations [--o=FILENAME]
        """
        filename = arg["--o"]

        dojo.print_allocations(filename)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """
        This commands prints a list of unallocated  to the screen specifying
        the optional --o 

        It simply takes the name of the file to save the unallocated printout
        If not provided, the printout will not be saved to a file.

        All allocations files are saved in the root directory.

        Usage: print_unallocated [--o=FILENAME]
        """
        filename = arg["--o"]

        dojo.print_unallocated(filename)

    @docopt_cmd
    def do_load_people(self, arg):
        """
        This function reads a lists of people and allocates them a room
        All input files are located inthe root directory
        
        Usage: load_people <file_name>
        """
        filename = arg['<file_name>']

        dojo.load_people(filename)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """
        This command reallocates a person to another room.

        It takes thes person's name which can be gotten from the list of
        allocations in a particular room when print_allocations is run

        The it takes is the name of the room to which you want
        to allocate the person to.

        Note: The argument <new_room_name> is case sensitive 

        Usage: reallocate_person <first_name> <last_name> <new_room_name>
        """
        name = arg['<first_name>'] + " " + arg["<last_name>"]
        new_room_name = arg['<new_room_name>']
        dojo.reallocate_person(name, new_room_name)

    @docopt_cmd
    def do_save_state(self, arg):
        """
        This command persists the current state of the system to an SQLite
        Database.

        It takes an option '<database_name>' which specifies the name to give the
        database file which we will use to save the state of the applicaion.
        If no DB name is given, the state is saved in a file named 'Dojo'

        Note: All DB files are saved in the root directory.

        Usage: save_state [<database_name>]

        """
        db_name = arg['<database_name>']
        if db_name:
            dojo.save_state(db_name)
        else:
            dojo.save_state('dojo')


   	# @docopt_cmd
	# def do_load_state(self, arg):

	# 	"""
	# 	Loads data from the specified db into the app.
	# 	Usage: load_state <filename>
	# 	"""
	# 	dojo.load_state(arg["<filename>"])

    @docopt_cmd
    def do_load_state(self, arg):
        """
        This command loads a previously saved state from an SQLite database to
        the System.

        It takes an argument, <sqlite_database> which specifies the name of the
        SQLite database file to load the state from.

        NB: All DB files are loaded from the root directory.

        Usage: load_state [<database_name>]
        """

        db_name = str(arg['<database_name>'])
        dojo.load_state(db_name)


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    start()
    Interactive().cmdloop()

print(opt)