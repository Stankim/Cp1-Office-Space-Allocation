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
    
    def __init__(self, name):
        self.name = name
        self.wants_accomodation = 'N'

    def __repr__(self):
        return '<Person %s>' % self.name

class Fellow(Person):
    
    def __init__(self, name):
        super(Fellow, self).__init__(name)
        


    def __repr__(self):
        return '<Fellow %s>' % self.name

class Staff(Person):
    
    def __init__(self, name):
        super(Staff, self).__init__(name)

    def __repr__(self):
        return '<Staff %s>' % self.name