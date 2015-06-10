
"""import the sqlalchemy library"""
from sqlalchemy import Column, Integer, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base

"""create the base class"""
Base = declarative_base()

"""create class active"""
class Login(Base):
    """limited table for test"""
    #__tablename__ = 'runcoollogin_log_10000'
    
    """complete table"""
    __tablename__ = 'runcoollogin_log'
    
    id = Column(Integer, primary_key = True)
    phoneUuid = Column(VARCHAR(64))
    userId = Column(Integer)
    loginType = Column(Integer)
    platform = Column(VARCHAR(32))
    vendor = Column(VARCHAR(32))
    model = Column(VARCHAR(32))
    gameName = Column(VARCHAR(32))
    version = Column(VARCHAR(32))
    time = Column(VARCHAR(32))
    
"""connect to mysql server
   change ****** to your local password"""
engine = create_engine('mysql+mysqlconnector://root:******@localhost:3306/runcool_assistant_log')
