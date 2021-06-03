import datetime
print(datetime.datetime.now()) #returns date & time as yyyy-mm-dd hh:mm:ss.microseconds

print(datetime.datetime.fromtimestamp(0)) #takes no of seconds, returns date =1970-01-01 05:30:00 + no of seconds

dt = datetime.datetime.now()    # returns datetime object
print(dt.hour,dt.minute,dt.second)

#timedelta Data Type
datedelta = datetime.timedelta(days=3,hours=10)
print(datedelta)
print(datedelta+datetime.datetime.now()) #gives new date after delta

datedelta = datetime.timedelta(weeks=5,days=10,hours=11,minutes=21,seconds=25,milliseconds=10,microseconds=19)
print(datedelta+datetime.datetime.now())

#Pausing untill a Specific Date
#import datetime

import time
diwali2021 = datetime.datetime(2021,11,10,0,0,0)
# while datetime.datetime.now()<diwali2021:
#     time.sleep(1)
#     print("HappyDiwali")

##Converting datetime objects into String
# %Y - like 2019           , %y like 99 or 01
# %B - like October        , %b like Nov ,     %m like 01 for January
# %d - day like 01 to 31   , %j like day of year 01 to 366
# %w - day of week like 0(Sunday) to 6(Saturday)
# %A - Full Weekday name - Monday etc     %a - like Mon
# %H - 00 to 23            , %h - 01 to 12 for am/pm
# %M - 00 to 59 min        , %S - seconds 00 to 59
# %p - pm/am
# %% - literal % character

date_time  = datetime.datetime(2021,11,10,1,5,55)
strdatetime = date_time.strftime('%Y/%m/%d %H:%M:%S')
print("date_time : ",date_time)
print("string form of date_time : ",strdatetime)

##Converting String into Datetime object - refer to above list
print(datetime.datetime.strptime('October 21, 2019','%B %d, %Y')) #please mind space
print(datetime.datetime.strptime('2019/10/11 16:20','%Y/%m/%d %H:%M'))
print(datetime.datetime.strptime("November of '63","%B of '%y"))






