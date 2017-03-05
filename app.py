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
from docopt import docopt, DocoptExit
from App.dojo import Dojo
from App.person import Fellow, Staff
from pyfiglet import figlet_format
from termcolor import cprint
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


class Interactive (cmd.Cmd):
    cprint(figlet_format(' THE DOJO', font='univers'), 'yellow', attrs=['bold'])
    intro = 'Welcome to Dojo office allocation!' \
        + ' (type help for a list of commands.)'
    prompt = '(dojo) '
    file = None
    

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_name> <room_type>"""
        name = arg['<room_name>']
        type_room  = arg['<room_type>']

        create_room_status = dojo.create_room(name, type_room)
        if create_room_status == 'Invalid Room Type':
            print(create_room_status)
            return
        # print (dojo.all_rooms)

        
    @docopt_cmd
    def do_add_person(self, arg):
        """
        Creates a person and assign them to a room in Dojo.
        Usage:
            add_person <first_name> <last_name> <role> [<accomodation>]
        """
        name = arg['<first_name>'] + " " + arg["<last_name>"]
        role = arg['<role>']
        wants_accomodation = arg['<accomodation>']

        dojo.add_person(name, role, wants_accomodation)

    @docopt_cmd
    def do_print_room(self, arg):
        """
        This function prints the members of a given room
        Usage:
            print_room [<room_name>]
        """
        room_name = arg['<room_name>']

        dojo.print_room(room_name)        


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Interactive().cmdloop()

print(opt)