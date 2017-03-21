[![Build Status](https://travis-ci.org/jimmykimani/Office-Space-Allocation.svg?branch=master)](https://travis-ci.org/jimmykimani/Office-Space-Allocation)
[![Waffle.io](https://img.shields.io/waffle/label/evancohen/smart-mirror/in%20progress.svg?style=flat-square)]()
[![Coverage](https://img.shields.io/badge/coverage-85%25-green.svg)]()
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square)]()
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()
[![Jimmy Kimani](https://img.shields.io/badge/Jmmy%20Kimani-Andela21-green.svg)]()

# THE DOJO OFFICE SPACE AllOCATION SYSTEM

The Dojo is an [Andela](http://andela.com) facility that has several rooms in it. A room can be
either a **Living Space** or an **Office Space**. An Office Space can accomodate a maximum of
6 people and the Living Space can accomodate a maximum of 4 at ago.  

The The Dojo Office Space Allocation allocates people either The Living Space or The Office Space randomly  

A room can be allocated **ONLY** to a staff or a fellow at Andela. Staff cannot be allocated living spaces.
 Fellows have a choice to choose a living space or not.

>The project is done in fulfillment of the Andela 21 project 2017

## 1 Installation

Clone this repo:
```
$ git clone https://github.com/jimmykimani/Office-Space-Allocation.git
```
```
$ git checkout develop
```

Navigate to the `Office-Space-Allocation.` directory:
```
$ cd Office-Space-Allocation.
```

Create a vitual environment:
> Use [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/) to create and activate a virtual environment.

Install the required packages:
```
$ pip install -r requirements.txt 

```
Run the app
```
$ `python app.py --i`
```

## 2 Commands

Command | Argument | Example
--- | --- | ---
create_room | livingspace or office | create_room Hogwarts office
add_person | (first_name) (last_name) (category) [--wants_accomodation |add_person John Doe fellow Y
reallocate_person | (Name) (new_room_name) | reallocate_person John Doe swift (Note cases!)
load_people | (filename) | load_people sample(txt)
print_allocations| [--o=filename] | print_allocations --o=allocations
print_unallocated| [--o=filename] | print_unallocated --o=unallocated
print_room | (room_name) | print_room Hogwarts
save_state | [--db=sqlite_database]| save_state Dojo
load_state |(sqlite_database)|load_state Dojo

The following screencast shows how to run the different commands. Check it out:
[![asciicast](https://asciinema.org/a/b870juwbzni440hsa4tkzxfj0.png)](https://asciinema.org/a/b870juwbzni440hsa4tkzxfj0?speed=2)

## 3 Usage

Launch the app in interactive mode:
```
$ python app.py -i
===========================================================================
   
oooooooooo.                 o8o           
`888'   `Y8b                `"'           
 888      888  .ooooo.     oooo  .ooooo.  
 888      888 d88' `88b    `888 d88' `88b 
 888      888 888   888     888 888   888 
 888     d88' 888   888     888 888   888 
o888bood8P'   `Y8bod8P'     888 `Y8bod8P' 
                            888           
                        .o. 88P           
                        `Y888P            

===========================================================================
   
Welcome to the Dojo office allocation! (type help for a list of commands.)
   
```
### Create Room
```
create_room <room_name> <room_type>
```
This command creates rooms in The Dojo
You can create  rooms by specifying room names
after the create_room command. By default, this method will create an
Office/Livingspace into the system.

```
The Dojo > create_room hogwarts office
    
 An office called Hogwarts has been successfully created!
    
The Dojo > create_room swift livingspace
    
 A Livingspace called Swift has been successfully created!

```

### Add Person
```
dd_person <first_name> <last_name> <role> [<accomodation(Y/N)>]
```
This command adds a person and allocates them a random room in The Dojo

The <role> argument specifies the role of the person being added
which can either be 'Fellow' or 'Staff'.

The <wants_accommodation> Here is an option argument which can
be either Y or N. The default value if not provided is N


Adding a Fellow with accomodation option:
```
The Dojo > add_person john doe fellow Y
ADDING JOHN DOE  ...
    
Fellow John doe has been successfully added ! 
John doe has been allocated to :
Office: Hogwarts 
ALLOCATING LIVINGSPACE ...
    
Livingspace: Swift

```
Adding a Staff:
```
The Dojo > add_person matial carter staff
ADDING MATIAL CARTER  ...
    
Staff Matial carter has been successfully added ! 
Matial carter has been allocated to :
Office: Hogwarts 

```
### Print Room
```
print_room <room_name>
```
This commands prints room details.

It accepts a room name then querries System and returns
information about the room given.
```
The Dojo > print_room hogwarts
PRINTING ROOM HOGWARTS  ...
 
====================
Hogwarts 
====================
John doe
Matial carter
Oluwafemi sule
Dominic walters
Simon patterson
Mari lawrence
====================
    
The Dojo > 

```

### Print Allocations
```
print_allocations [--o=FILENAME]
```
This commands prints a list of allocations to the screen specifying
the optional --o 

It simply takes the name of the file to save the allocations printout
If not provided, the printout will not be saved to a file.

All allocations files are saved in the root directory.
```
The Dojo > print_allocations
PRINTING ALLOCATIONS...
 
=========================
HOGWARTS  | Office
=========================
John doe (Fellow)
Matial carter (Staff)
Oluwafemi sule (Fellow)
Dominic walters (Staff)
Simon patterson (Fellow)
Mari lawrence (Fellow)
=========================
SWIFT  | Livingspace
=========================
John doe (Fellow)
Oluwafemi sule (Fellow)
Simon patterson (Fellow)
Mari lawrence (Fellow)

```
### Print unallocated
```
print_unallocated [--o=FILENAME]
```
This commands prints a list of unallocated  to the screen specifying
the optional --o 

It simply takes the name of the file to save the unallocated printout
If not provided, the printout will not be saved to a file.

All allocations files are saved in the root directory.

```
The Dojo > print_unallocated
====================
Unallocated People
====================
Leigh riley
Tana lopez
Tana lopez
Kelly Mcguire

```
### Reallocate Person
```
reallocate_person <first_name> <last_name> <new_room_name>
```

This command reallocates a person to another room.

It takes thes person's name which can be gotten from the list of
allocations in a particular room when print_allocations is run

The it takes is the name of the room to which you want
to allocate the person to.

Note: The argument <new_room_name> is case sensitive.
```
The Dojo > reallocate_person john doe hogwarts
john doe has been reallocated to hogwarts
The Dojo > print_allocations
PRINTING ALLOCATIONS...
 
=========================
HOGWARTS  | Office
=========================
John doe (Fellow)
=========================
CAMELOT  | Office
=========================
There are no people yet.

```
### Save State
```
save_state [<database_name>]
```
This command persists the current state of the system to an SQLite
Database.

It takes an option '<database_name>' which specifies the name to give the
database file which we will use to save the state of the applicaion.
If no DB name is given, the state is saved in a file named 'Dojo'

Note: All DB files are saved in the root directory.

```
The Dojo > save_state
Data added to dojo database successfully

```
### Load State
```
load_state [<database_name>]
```
This command loads a previously saved state from an SQLite database to
the System.

It takes an argument, <sqlite_database> which specifies the name of the
SQLite database file to load the state from.

NB: All DB files are loaded from the root directory.

```
The Dojo > load_state
Database does not exist
The Dojo > load_state dojo
    
 An office called Hogs has been successfully created!
    
    
 An office called Swift has been successfully created!
    
    
 An office called Camelot has been successfully created!
    
Load successful!
The Dojo > print_allocations
PRINTING ALLOCATIONS...
 
=========================
HOGS  | Office
=========================
There are no people yet.
=========================
SWIFT  | Office
=========================
Kelly mcguire (Staff)
=========================
CAMELOT  | Office
=========================
Dominic walters (Staff)
Leigh riley (Staff)

```
### Tests.

To run Pytest ensure that you are within the *virtual environment* and have the following installed:

1. *Pytest*

2. *coveralls*


After that make sure you within the ** Office allocation  folder** run :
```
jimkaks@jimmy:~/Desktop/Office-Space-Allocation$ python -m pytest
===================================================================================================== test session starts ======================================================================================================
platform linux2 -- Python 2.7.12, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
rootdir: /home/jimkaks/Desktop/Office-Space-Allocation, inifile: 
collected 25 items 

tests/test_dojo.py .........................

================================================================================================== 25 passed in 2.88 seconds ==================================================================================================
jimkaks@jimmy:~/Desktop/Office-Space-Allocation$ 
```
## Credits

1. [Jimmy Kimani](https://github.com/jimmykimani)

2. [Andela](https://www.andela.com) community.

3. [Andela 21](https://www.andela.com) community.


## License

### The MIT License (MIT)

Copyright (c) 2017 [JImmy Kimani](https://github.com/jimmykimani).

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
