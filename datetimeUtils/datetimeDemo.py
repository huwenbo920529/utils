#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 15:32 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : datetimeDemo.py 
# @Software: PyCharm Community Edition
import datetime
import time

# datetime.datetime.now().date() 等价于datetime.date.today()
# print (now_day-b).days
# 1.time相关的
timestamp = time.time()  # 当前时间戳
print timestamp

time_tuple = time.localtime(timestamp)  # 时间元组
# 序号	属性	    值
# 0	    tm_year	    2008
# 1	    tm_mon	    1 到 12
# 2	    tm_mday	    1 到 31
# 3	    tm_hour	    0 到 23
# 4	    tm_min	    0 到 59
# 5	    tm_sec	    0 到 61 (60或61 是闰秒)
# 6	    tm_wday	    0到6 (0是周一)
# 7	    tm_yday	    一年中的第几天，1 到 366
# 8	    tm_isdst    是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
print time_tuple


time_format1 = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)  # 将时间元组转换成某种格式的时间形式展示
time_format2 = time.strftime("%A %B %d %H:%M:%S %Y %p", time_tuple)
time_format3 = time.strftime("%Y-%m-%d %H:%M:%S %B %A %j %U %w %W %c %p", time_tuple)
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
print time_format1
print time_format2
print time_format3


# 2.datetime相关
my_datetime = datetime.datetime(year=2018, month=7, day=19, hour=18, minute=25, second=12, microsecond=121213)  # 通过指定年月日时分秒微秒来构造datetime.datetime对象
timestamp = time.time()
my_datetime2 = datetime.datetime.fromtimestamp(timestamp)  # 从当前时间戳构造datetime.datetime对象
time_str = '2018-07-10 18:57:34'
my_datetime3 = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')  # 从指定格式的字符串构造datetime.datetime对象
print my_datetime, my_datetime2, my_datetime3
now_datetime = datetime.datetime.now()  # 直接通过当前时间构造datetime.datetime对象
print now_datetime, type(now_datetime)
# 相差的天数，秒数以及微秒数可以直接算，其他的好像不太适用
print (my_datetime - my_datetime3).days
print (my_datetime - my_datetime3).seconds
print (my_datetime - my_datetime3).microseconds


my_data1 = datetime.date(year=2018, month=7, day=17)  # 直接构造
my_data2 = my_datetime.date()  # 获取年月日部分,得到datetime.data对象
print my_data2, type(my_data2)
print (my_data1 - my_data2).days  # 计算相差多少天

my_time1 = datetime.time(hour=18, minute=25, second=12, microsecond=121213)  # 直接构造
my_time2 = my_datetime.time()  # 获取时分秒（微秒）部分，得到datetime.time对象
print my_time2, type(my_time2)
# ---------print (my_time1 - my_time2).minutes---------此方法不适用

datetime_timedelta = my_datetime + datetime.timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5, microseconds=6)
print datetime_timedelta

after_week = my_datetime + datetime.timedelta(weeks=1)  # 一个星期后
print after_week, type(after_week)
after_oneday = my_datetime + datetime.timedelta(days=1)  # 一天后
print after_oneday, type(after_oneday)
after_fivehours = my_datetime + datetime.timedelta(hours=5)  # 5个小时之后
print after_fivehours, type(after_fivehours)
after_tenminutes = my_datetime + datetime.timedelta(minutes=10)  # 10分钟之后
print after_tenminutes, type(after_tenminutes)
after_tenseconds = my_datetime + datetime.timedelta(seconds=10)  # 10秒之后
print after_tenseconds, type(after_tenseconds)
after_tenmicroseconds = my_datetime + datetime.timedelta(microseconds=10)  # 10微秒之后
print after_tenmicroseconds, type(after_tenmicroseconds)


# datetime.data对象
after_week_my_data1 = my_data1 + datetime.timedelta(weeks=1)  # 一个星期后
print after_week_my_data1, type(after_week_my_data1)
after_oneday_my_data1 = my_data1 + datetime.timedelta(days=1)  # 一天后
print after_oneday_my_data1, type(after_oneday_my_data1)


# datetime.time对象, 以下方法不可用
# after_fivehours_my_time1 = my_time1 + datetime.timedelta(hours=5)  # 5个小时之后
# print after_fivehours_my_time1, type(after_fivehours_my_time1)
# after_tenminutes_my_time1 = my_time1 + datetime.timedelta(minutes=10)  # 10分钟之后
# print after_tenminutes_my_time1, type(after_tenminutes_my_time1)
# after_tenseconds_my_time1 = my_time1 + datetime.timedelta(seconds=10)  # 10秒之后
# print after_tenseconds_my_time1, type(after_tenseconds_my_time1)
# after_tenmicroseconds_my_time1 = my_time1 + datetime.timedelta(microseconds=10)  # 10微秒之后
# print after_tenmicroseconds_my_time1, type(after_tenmicroseconds_my_time1)
