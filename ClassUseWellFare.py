
"""import the sqlalchemy library"""
from sqlalchemy import Column, Integer, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base

"""create the base class"""
Base = declarative_base()

"""create class active"""
class UseWellFare(Base):
    __tablename__ = 'runcool_usewellfare_log'
    
    id = Column(Integer, primary_key = True)
    userId = Column(Integer)
    date = Column(VARCHAR(32))
    perType = Column(Integer)
    type = Column(Integer)
    wellId = Column(Integer)
    remainCount = Column(Integer)
    percentCount = Column(Integer)
    
"""connect to mysql server
   change ****** to your local password"""
engine = create_engine('mysql+mysqlconnector://root:******@localhost:3306/runcool_analysis')
