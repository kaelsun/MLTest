"""
Classes that start with "Class" defines the original database
by: zyguo
"""

# import the sqlalchemy library
from sqlalchemy import Column, Integer, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base

# create the base class
Base = declarative_base()

# create class recharge
class Recharge(Base):
    __tablename__ = 'runcoolrecharge_log'
    
    id = Column(Integer, primary_key = True)
    userId = Column(Integer)
    time = Column(VARCHAR(32))
    currency = Column(Integer)
    currencyMount = Column(Integer)
    type = Column(Integer)
    amount = Column(Integer)
    version = Column(VARCHAR(50))
    
# connect to mysql server
# change ****** to your local password
engine = create_engine('mysql+mysqlconnector://root:******@localhost:3306/runcool_analysis')
