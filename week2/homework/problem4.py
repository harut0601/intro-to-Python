import datetime
import calendar
import time

bday_datetime = datetime.date(2003, 1, 6)
print(bday_datetime)

print(bday_datetime.year)
print(bday_datetime.day)
print(bday_datetime.weekday())

final = datetime.date.today() - bday_datetime
print(final)

cal = calendar.month(2017,5)
print ("The calendar: ")
print (cal)

print("Yesterday date:", datetime.date.today() - datetime.timedelta(days=1))
print("Time now:", datetime.datetime.now().time())
print("2 days more:", datetime.date.today() - datetime.timedelta(days=1) + datetime.timedelta(days=2))
print("3 days less:", datetime.date.today() - datetime.timedelta(days=1) - datetime.timedelta(days=3))