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
    def __init__(self, name,capacity):
        self.name = name
        self.capacity = capacity
        self.members = []

    def __repr__(self):
        return '<Room %s >' % self.name

    def add_person(self,person):
        self.capacity = self.capacity -1
        return self.capacity

    @property
    def room_type(self):
        return self.__class__.__name__

class Office(Room):

    '''
    initialization module
    '''

    def __init__(self, name):
        super(Office, self).__init__(name, capacity=6)

    def __repr__(self):
        return '<Office %s >' % self.name


class Livingspace(Room):
    
    '''
    initialization module
    '''    

    def __init__(self, name):
        super(Livingspace, self).__init__(name, capacity=4)

    def __repr__(self):
        return '<Livingspace %s >' % self.name
    