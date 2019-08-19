#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 17:31 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : calendarDemo.py 
# @Software: PyCharm Community Edition
import calendar

# 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。
# 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
year_cal = calendar.calendar(2018, w=2, l=1, c=6)
print(year_cal)

# 获取某年某月的日历
cal = calendar.month(2018, 2)
print(cal)

# 判断是否是瑞年
bool = calendar.isleap(2018)
print(bool)

# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）
weekday = calendar.weekday(2018, 1, 25)
print(weekday)
