from sqlalchemy import Column, Date, String, Integer
from base import Base 


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday