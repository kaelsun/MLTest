
"""import the sqlalchemy library"""
from sqlalchemy import Column, Integer, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base

"""create the base class"""
Base = declarative_base()

"""create class active"""
class Active(Base):
    """limited table for test"""
    __tablename__ = 'runcoolactive_log_10000'
    
    """complete table"""
    #__tablename__ = 'runcoolactive_log'
    
    id = Column(Integer, primary_key = True)
    userId = Column(Integer)
    time = Column(VARCHAR(32))
    state = Column(Integer)
    
"""connect to mysql server
   change ****** to your local password"""
engine = create_engine('mysql+mysqlconnector://root:******@localhost:3306/runcool_analysis')
