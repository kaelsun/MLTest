
# import the sqlalchemy library
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *
import ClassActive

Active = ClassActive.Active
engine = ClassActive.engine

#create DBSession
DBSession = sessionmaker(bind=engine)
session = DBSession()

activelist = list()
for imp in session.query(Active.userId, func.count(Active.userId)).group_by(Active.userId).all():
    active = int(imp[1])
    activelist.append(active)
    
hist(activelist, bins = 200);
show()

session.close()