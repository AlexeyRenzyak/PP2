import datetime

""" #1
date = datetime.datetime.now()
date += datetime.timedelta(-5)
print(date.day, date.month, date.year) """

""" #2
date = datetime.datetime.now()
datey = date + datetime.timedelta(-1)
datet = date + datetime.timedelta(1)
print("Yesterday:", datey.day, datey.month, datey.year)
print("Today:", date.day, date.month, date.year)
print("Tomorrow:", datet.day, datet.month, datet.year) """

""" #3
date = datetime.datetime.now()
date = date.replace(microsecond=0)
print(date) """

""" #4
date1 = datetime.datetime.now()
date2 = date1 + datetime.timedelta(hours=101, weeks=1)
print(abs(date1.timestamp()-date2.timestamp())) """