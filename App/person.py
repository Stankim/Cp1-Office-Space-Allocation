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
    
    def __init__(self, person_name, category):
        self.name = person_name
        self.category = category

    def __repr__(self):
        return '<Person %s>' % self.name

class Fellow(Person):
    
    def __init__(self, name, wants_accomodation='N'):
        super(Fellow, self).__init__(name)
        self.wants_accomodation= wants_accomodation

    def __repr__(self):
        return '<Fellow %s>' % self.name
    


class Staff(Person):
    
    def __init__(self, name):
        super(Staff, self).__init__(name)

    def __repr__(self):
        return '<Staff %s>' % self.name