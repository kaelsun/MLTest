
# import the sqlalchemy library
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *
import ClassGetWellFare
import ClassUseWellFare
import time
import datetime

Get = ClassGetWellFare.GetWellFare
engineG = ClassGetWellFare.engine

Use = ClassUseWellFare.UseWellFare
engineU = ClassUseWellFare.engine

#create DBSession
DBSession = sessionmaker(bind=engineG)
sessionG = DBSession()

DBSession = sessionmaker(bind=engineU)
sessionU = DBSession()

listG = sessionG.query(Get.perType, func.count(func.distinct(Get.userId))).group_by(Get.perType).all()
listU = sessionU.query(Use.perType, func.count(func.distinct(Use.userId))).group_by(Use.perType).all()

"""
mapG = {}
mapU = {}
for g in listG:
    mapG[g[0]] = g[1]
for u in listU:
    mapU[u[0]] = u[1]
"""

keylist = list()
valuelist = list()
for g in listG:
    keylist.append(g[0])
    valuelist.append(g[1])
for u in listU:
    keylist.append(u[0])
    valuelist.append(u[1])

print(listG)
print(listU)

bar(keylist, valuelist, width=0.5, color='y')
show()

sessionG.close()
sessionU.close()
