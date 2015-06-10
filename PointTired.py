
# import the sqlalchemy library
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *
import ClassActive
import time
import datetime

Active = ClassActive.Active
engine = ClassActive.engine

#create DBSession
DBSession = sessionmaker(bind=engine)
session = DBSession()

durationlist = list()
for imp in session.query(Active.userId, func.max(Active.time), func.min(Active.time)).group_by(Active.userId).all():
    #print(1, imp[1])
    #print(2, imp[2])
    """from time string to time stamp for calculation"""
    max = time.mktime(time.strptime(imp[1], '%Y-%m-%d %H:%M:%S'))
    min = time.mktime(time.strptime(imp[2], '%Y-%m-%d %H:%M:%S'))
    duration = max - min
    if duration > 0:
        durationlist.append(duration)
    #print(3, max)
    #print(4, min)
    
hist(durationlist, bins = 2000);
show()

session.close()