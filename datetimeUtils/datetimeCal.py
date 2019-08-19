#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 15:42 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : datetimeCal.py 
# @Software: PyCharm Community Edition
import datetime


# 1.将“2019-08-19T10:10:10”转成dateTime类型
time_str = "2019-08-19T10:10:10"
t1 = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")

# 2.按天-天计算时间差值
now_date1 = datetime.datetime.now().date()
t_date1 = t1.date()
diff_days = (now_date1 - t_date1).days

# 3.按相差24小时才算一天，计算时间差值
now_date2 = datetime.datetime.now()
t_date2 = t1
diff_days2 = (now_date2 - t_date2).days


# def trans_date_format(date_str):
#     """
#     将yyyy-MM-ddThh:mm:ss转换成：MM-dd-yyyy hh:mm格式
#     :param date_str:
#     :return:
#     """
#     if date_str:
#         if 'T' in date_str:
#             ymd, hms = date_str.split('T')
#             year, month, day = ymd.split('-')
#             if hms:
#                 hour, minute, second = hms.split(':')
#                 date_str = '-'.join([month, day, year]) + ' ' + ':'.join([hour, minute])
#             else:
#                 date_str = '-'.join([month, day, year])
#         else:
#             year, month, day = date_str.split('-')
#             date_str = '-'.join([month, day, year])
#     return date_str
