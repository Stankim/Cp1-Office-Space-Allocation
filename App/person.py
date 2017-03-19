"""
File      : person.py
Date      : March, 2017
Author(s) : Jimmy Kimani <jimmykkimani@gmail.com>
Desc      : Office Allocator person module
"""
class Person(object):
    
    '''
    This creates a Room object where the class Office
    and Livingspace inherit from
    '''   
    def __init__(self, name, wants_accomodation):
        self.name = name
        self.wants_accomodation = wants_accomodation
        self.office = None

    def __repr__(self):
        return '<Person %s>' % self.name

    @property
    def room_type(self):
        return self.__class__.__name__
        
class Fellow(Person):

    person_type = 'Fellow'

    def __init__(self, name,wants_accomodation=''):
        super(Fellow, self).__init__(name, wants_accomodation)
        self.livingspace = None

    def __repr__(self):
        return '<Fellow %s>' % self.name

class Staff(Person):
    
    person_type = 'Staff'

    def __init__(self, name, wants_accomodation='N'):
        super(Staff, self).__init__(name, wants_accomodation)
        self.livingspace = None

    def __repr__(self):
        return '<Staff %s>' % self.name