import random
import datetime
PERS = ['TOTO', 'TATA', 'BULB']
COUN = ['FRA','BMU','BEL','HND']
date = datetime.datetime.now ()
delta = datetime.timedelta(0,50) # 50 sec
million = 1000000
f = open ("transactions.csv","w")
for i in range (10 * million):
  frm   = random.choice (PERS)
  to     = random.choice (PERS)
  amount = random.random () * 100
  date   += delta
  c1 = random.choice (COUN)
  c2 = random.choice (COUN)
  f.write ("{},{},{},{},{},{},{}\n".format( i, frm, to, amount, date, c1, c2))
f.close ()
