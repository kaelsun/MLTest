
# import the sqlalchemy library
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *
import ClassLogin
import ClassRecharge
import time

Login = ClassLogin.Login
Recharge = ClassRecharge.Recharge

engineL = ClassLogin.engine
engineR = ClassRecharge.engine

DBSession = sessionmaker(bind=engineL)
sessionL = DBSession()
DBSession = sessionmaker(bind=engineR)
sessionR = DBSession()

#listL = sessionL.query(Login.userId, func.min(Login.time)).group_by(Login.userId).all()
#listR = sessionR.query(Recharge.userId, func.min(Recharge.time)).group_by(Recharge.userId).all()

"""number of lines in table login"""
loginamount = sessionL.query(func.count(Login.id)).all()[0][0]
time = loginamount // 10000 + 1

listL = list()
for i in range(0, time):
    listL += sessionL.query(Login.userId, func.min(Login.time)).group_by(Login.userId)[i * 10000 : i * 10000 + 10000]

#listL = sessionL.query(Login.userId, func.min(Login.time)).group_by(Login.userId).limit(10000)
listR = sessionR.query(Recharge.userId, func.min(Recharge.time)).group_by(Recharge.userId).limit(10000)


mapL = {}
for a in listL:
    mapL[a[0]] = a[1]
    
durationlist = list()
for r in listR:
    if  r[0] in mapL.keys():
        max = time.mktime(time.strptime(r[1], '%Y-%m-%d %H:%M:%S'))
        min = time.mktime(time.strptime(mapL.get(r[0]), '%Y-%m-%d %H:%M:%S'))
        durationlist.append(max - min)
        
hist(durationlist, bins=2000)
show()

sessionL.close()
sessionR.close()

