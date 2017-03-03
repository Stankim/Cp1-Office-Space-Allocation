"""
File      : rooms.py
Date      : March, 2017
Author(s) : Jimmy Kimani <jimmykkimani@gmail.com>
Desc      : Office Allocator rooms module
"""
class Room(object):
    '''
    This creates a Room object where the class Office
    and Livingspace inherit from
    '''
    def __init__(self, name):
        self.name = name
        self.members = []

    def __repr__(self):
        return '<Room %s >' % self.name

class Office(Room):

    capacity = 6
    '''
    initialization module
    '''

    def __init__(self, name):
        super(Office, self).__init__(name)

    def __repr__(self):
        return '<Office %s >' % self.name


class Livingspace(Room):

    capacity = 4

    def __init__(self, name):
        super(Livingspace, self).__init__(name)

    def __repr__(self):
        return '<Livingspace %s >' % self.name
    