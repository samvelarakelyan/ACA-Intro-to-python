import datetime
import time
import calendar

"""
2)
-------------
"""
#a)
date_time=datetime.datetime.today()
print("Date and Time:",date_time)

#b)
year=date_time.year
print("Year:",year)

#c)
month=date_time.month
print("month:",month)

#d)
today=datetime.date.today()
wd0=today.weekday()
wd1=today.isoweekday()
wd_name=calendar.day_name[wd0]

print("Weekday:",wd0,"or",wd1,"i.e.",wd_name)


"""
3)
"""
today=datetime.datetime.today() 
days=datetime.timedelta(days=5)
delta=today-days

print(delta)

"""
4
"""
today=datetime.datetime.today()
seconds=datetime.timedelta(seconds=5)
delta=today+seconds

print(delta)