#print('Hello World')
"""
Classes start with "Point" do the database analysis
by: zyguo
"""

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

"""#for test
query = session.query(Recharge.userId, Recharge.currencyMount).filter('userId = 10')
for recharge in query:
    #print(recharge.userId)
    #print(recharge.currencyMount)
    print(recharge[0])
    print(recharge[1])
"""
#session.execute()
"""
query_userid = session.query(Recharge.userId).order_by(Recharge.userId)
for id in query_userid:
    query_amount = session.query(Recharge).filter('userId = :param', {"param": id.userId})
    amount = 0
    for single_amount in query_amount:
        amount = amount + single_amount.currencyMount/10
    totalrecharge = TotalRecharge(id.userId, amount)
    print('userid:', totalrecharge.userid)
    print('totalamount:', totalrecharge.amount)
"""


#useridlist = list()
amountlist = list()
for imp in session.query(Recharge.userId, func.sum(Recharge.currencyMount)).group_by(Recharge.userId).all():
    #print("userid:", imp[0])
    #print("total amount:", imp[1])
    if imp[1] > 0:
        #userid = imp[0]
        #useridlist.append(userid)
        amount = int(imp[1]/100)
        if amount < 1000:
            amountlist.append(amount)


#plot(useridlist, amountlist)
#histogram(amountlist)
hist(amountlist, bins = 1000)
#print(amountlist)
show()

#print 'userid', recharge.userId
#print 'currencyMount', recharge.currencyMount
#print(recharge.userId)
#print(recharge.currencyMount)

session.close()
