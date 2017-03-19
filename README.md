[![Build Status](https://travis-ci.org/jimmykimani/Office-Space-Allocation.svg?branch=master)](https://travis-ci.org/jimmykimani/Office-Space-Allocation)
[![Waffle.io](https://img.shields.io/waffle/label/evancohen/smart-mirror/in%20progress.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square)]()
[![Coverage Status](https://coveralls.io/repos/github/jimmykimani/Office-Space-Allocation/badge.svg?branch=master)](https://coveralls.io/github/jimmykimani/Office-Space-Allocation?branch=develop)

# THE DOJO OFFICE SPACE AllOCATION SYSYTEM

The Dojo is an [Andela](http://andela.com) facility that has several rooms in it. A room can be
either a **Living Space** or an **Office Space**. An Office Space can accomodate a maximum of
6 people and the Living Space can accomodate a maximum of 4 at ago.  

The The Dojo Office Space Allocation allocates people either The Living Space or The Office Space randomly  

A room can be allocated **ONLY** to a staff or a fellow at Andela. Staff cannot be allocated living spaces.
 Fellows have a choice to choose a living space or not.


#1 Installation

Clone this repo:
```
$ git clone https://github.com/jimmykimani/Office-Space-Allocation.git
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

Run the app
```
$ `python app.py --i`


#2. Commands.

Command | Argument | Example
--- | --- | ---
create_room | livingspace or office | create_room Hogwarts office
add_person | (first_name) (last_name) (category) [--wants_accomodation |add_person John Doe fellow Y
reallocate_person | (Name) (new_room_name) | reallocate_person John Doe swift (Note cases!)
load_people | (filename) | load_people sample
print_allocations| [--o=filename] | print_allocations --o=allocations
print_unallocated| [--o=filename] | print_unallocated --o=allocations
print_room | (room_name) | print_room Fayetteville
save_state | [--db=sqlite_database]| save_state --db=carolina
load_state |(sqlite_database)|load_state my_newdatabase

