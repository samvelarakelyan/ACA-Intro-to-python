import calendar
import datetime 
import time

"""
2)
"""
#a)
print(datetime.date(2000,8,18))

#b)
print(datetime.date(2000,8,18).year)

#c)
print(datetime.date(2000,8,18).month)

#d)
print(datetime.date(2000,8,18).day)

#e)
wd_num=calendar.weekday(2000,8,18)
wd_name=calendar.day_name[wd_num]
print(wd_name)

#f)
# birthday_mounth=datetime.datetime(2000,8,18).month
# print(birthday_mounth)
# birthday_day=datetime.datetime(2000,8,18).day
# print(birthday_day)


# print(time.localtime())



year = int(input('please , input your birthyday (year)  ` '))
month = int(input('please , input your birthyday (month) ` '))
day = int(input('please , input your birthyday (day) ` '))

birthyday = datetime.datetime(year,month,day)
now = datetime.datetime.now()
birthday = datetime.datetime(now.year, birthyday.month, birthyday.day)
finaly = (birthday - now.today()).days + 1
 
print(finaly if finaly > 0 else 365 - abs(finaly),'days left until your next birthday')


"""
3)
"""
print(calendar.month(2017,5))

"""
4)
"""
today=datetime.datetime.today()
delta=datetime.timedelta(days=1)
yesterday=today-delta
print(yesterday)

 #a)
delta=datetime.timedelta(days=2)
print(yesterday+delta)

#b)
delta=datetime.timedelta(days=3)
print(yesterday-delta)

