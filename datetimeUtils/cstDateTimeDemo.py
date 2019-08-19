#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 15:40 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : cstDateTimeDemo.py 
# @Software: PyCharm Community Edition
import datetime
import pytz


def cst_date_time():
    # Convert UTC time to CST time (美国中部时间)
    current_utc_time = datetime.datetime.utcnow()
    current_utc_time = datetime.datetime.strptime(str(current_utc_time).split(".")[0], "%Y-%m-%d %H:%M:%S")
    cst_timezone = pytz.timezone('America/Chicago')
    current_cst_time = current_utc_time.replace(tzinfo=pytz.utc).astimezone(cst_timezone)
    tmp = str(current_cst_time).split(" ")
    if "-" in tmp[1]:
        current_cst_time = datetime.datetime.strptime(tmp[0] + " " + tmp[1].split("-")[0], "%Y-%m-%d %H:%M:%S")
    elif "+" in tmp[1]:
        current_cst_time = datetime.datetime.strptime(tmp[0] + " " + tmp[1].split("+")[0], "%Y-%m-%d %H:%M:%S")
    return current_cst_time
