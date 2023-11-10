import datetime
import calendar
"""
datetime模块重新封装了time模块，提供更多接口，提供的类有date,time,datetime,timedelta等。
datetime模块中的datetime类
calendar模块：日历模块
"""
#根据给定的值，创建时间元组：datetime.datime(年、月、日、时、分、秒、微秒)
dt=datetime.datetime(2018,6,24,16,56,45,13)
print(dt)
print("now:",datetime.datetime.now())
dt=datetime.datetime.now()
print("year:",dt.year)
print("month:",dt.month)
print("second:",dt.second)
print("星期:",dt.weekday())

#将datetime转成字符串
print("将datetime转成字符串:",dt.strftime("%Y-%m-%d"))
print("将datetime转成字符串:",dt.strftime("%Y-%m-%d %H:%M:%S"))
print("datetime转换前类型：",type(dt))
print("datetime转换后类型：",type(dt.strftime("%Y-%m-%d %H:%M:%S")))

print("today:",datetime.datetime.today())

#.timestamp当前时间转成时间戳
print("timestamp:",datetime.datetime.timestamp(dt))

#.timestamp当前时间转成时间戳
timestamp=datetime.datetime.now().timestamp()
print("时间戳：",timestamp)
print("时间戳转换成当前时间：",datetime.datetime.fromtimestamp(timestamp))

#获取某年的年历
c1=calendar.calendar(2023)
print("年历：",c1)

#获取某年某月的日历,即月历
c2=calendar.month(2023,11)
print("月历\n",c2)

c3=calendar.weekday(2023,11,10)
print("指定年月日的星期：",c3)
