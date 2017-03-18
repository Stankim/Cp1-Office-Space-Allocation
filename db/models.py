from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rooms(Base):
    __tablename__='Dojorooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type_room = Column(String(250), nullable=False)
    room_capacity = Column(Integer)

    def __repr__(self):
        return '<Room (name=%s)>' % self.name


class Persons(Base):
    __tablename__='person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    category = Column(String(250), nullable=False)
    wants_accomodation = Column(String(25))
    office_allocated = Column(String(250))
    living_space_allocated = Column(String(250))

    def __repr__(self):
        return '<Person (name=%s)>' % self.name


def create_db(db_name):
    engine = create_engine('sqlite:///' + db_name)
    Base.metadata.create_all(engine)
    return engine
