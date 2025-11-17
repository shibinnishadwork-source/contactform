from sqlalchemy import Column,Integer,Text,String
from database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key =True )
    name = Column(String(100),nullable =False)
    email = Column(String(100),nullable =False )
    message = Column(Text,nullable =False )