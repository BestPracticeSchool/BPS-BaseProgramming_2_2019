from sqlalchemy import Column, String, Integer, ForeignKey
from base import Base 
from sqlalchemy.orm import relationship, backref

class ContactDetails(Base):
    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key = True)
    phone_number = Column(String)
    address = Column(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref="contact_details")

    def __init__(self, phone_number, address, actor):
        self.phone_number = phone_number
        self.address = address
        self.actor = actor