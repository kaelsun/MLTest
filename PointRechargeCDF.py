
# import the sqlalchemy library
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import ClassRecharge
import numpy as np
#import matplotlib.pyplot as plt
from pylab import *

Recharge = ClassRecharge.Recharge
engine = ClassRecharge.engine
    
# create class TotalRecharge
class TotalRecharge:
    
    def __init__(self, userid, amount):
        self.userid = userid
        self.amount = amount

#create DBSession
DBSession = sessionmaker(bind=engine)

session = DBSession()

#useridlist = list()
amountlist = list()
for imp in session.query(Recharge.userId, func.sum(Recharge.currencyMount)).group_by(Recharge.userId).all():
    if imp[1] > 0:
        amount = int(imp[1]/100)
        if amount < 200:
            amountlist.append(amount)

sorted = np.sort(amountlist)
"""Draw cdf"""
plt.plot(sorted, np.linspace(0, 1, sorted.size))

show()

session.close()
