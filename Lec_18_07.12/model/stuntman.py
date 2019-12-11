from sqlalchemy import Column, Boolean, String, Integer, ForeignKey
from base import Base 
from sqlalchemy.orm import relationship, backref

class Stuntman(Base):
    __tablename__ ='stuntmen'


    id = Column(Integer, primary_key = True)
    name = Column(String)
    active = Column(Boolean)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref = backref("stuntman", uselist = False))


    def __init__(self, name, active, actor):
        self.name = name
        self.active = active 
        self.actor = actor 
