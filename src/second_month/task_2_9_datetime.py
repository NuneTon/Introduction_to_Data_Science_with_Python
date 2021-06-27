import pandas as pd
import pytz
from datetime import datetime, timedelta
from tzlocal import get_localzone

#Task1
# Write a Pandas program to create
# a) Datetime object for Jan 15 2012.
# b) Specific date and time of 9:20 pm.
# c) Local date and time.
# d) A date without time.
# e) Current date.
# f) Time from a datetime.
# g) Current local time.

print(datetime(2012,1,15, 21,20).strftime('%Y-%m-%d %I:%M %p')) # a,b
utc_dt = datetime(2009, 7, 10, 18, 44, 59, 193982, tzinfo=pytz.utc)
print(utc_dt.astimezone(get_localzone())) #c
print(datetime.today().strftime("%d/%m/%Y")) # d
print(datetime.utcnow()) # e
print(datetime.now().strftime("%H:%M:%S")) #f
tz = pytz.timezone('Asia/Yerevan')
yerevan_now = datetime.now(tz) # g

#Task2
#Write a Pandas program to print the day after and before a specified date. Also print the days between two given dates.

date=datetime.today()
next_day=date+timedelta(days=1)
previous_day=date-timedelta(days=1)
print(next_day)
print(previous_day)
print(next_day-previous_day)

#Task3
#Write a Pandas program to create a date from a given year, month, day and another date from a given string format.
print(datetime(2020,6,5))
date_time_str = '18/09/19 01:55:19'
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
print(date_time_obj)

#Task4
#Write a Pandas program to create a date range using a startpoint date and a number of periods.

date_range=pd.date_range("2021-01-01", periods=5, freq="M")
print(date_range)

#Task5
# Write a Pandas program to create a time series using three months frequency.
date = pd.date_range("2018-01-01", periods=3, freq="M")
ts = pd.Series(range(len(date)), index=date)
print(ts)

