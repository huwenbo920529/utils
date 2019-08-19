#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 15:23 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : loogerDemo1.py 
# @Software: PyCharm Community Edition
import logging
from logging.handlers import TimedRotatingFileHandler


def func1():
    # 创建一个logger
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('test.log')
    fh.setLevel(logging.DEBUG)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    time_handler = TimedRotatingFileHandler("test2.log", 'midnight', 1, 0)
    formatter = logging.Formatter("[%(asctime)s] [%(funcName)s in %(filename)s:%(lineno)d] [%(levelname)s]:%(message)s")
    time_handler.setFormatter(formatter)
    time_handler.suffix = "%Y%m%d-%H%M.log"
    logger.addHandler(time_handler)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    # logger.removeHandler(fh)
    logger.addHandler(ch)
    return logger


logger1 = func1()
# 记录一条日志
# logger.info('foorbar')
# logger1.handlers.pop(1)


# # 日志
# def create_logger(log_name):
#     logger = logging.getLogger(log_name)
#     logger.setLevel(logging.DEBUG)
#
#     if not logger.handlers:
#         # The max size of the log file is 100M.
#         # If exceeded, a new one will be created.
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(logging.DEBUG)
#         formatter = logging.Formatter(
#             "[%(asctime)s] [%(funcName)s in %(filename)s:%(lineno)d] [%(levelname)s]:%(message)s")
#         console_handler.setFormatter(formatter)
#         time_handler = TimedRotatingFileHandler(log_name, 'midnight', 1, 0)
#         time_handler.setFormatter(formatter)
#         logger.addHandler(time_handler)
#         logger.addHandler(console_handler)
#     return logger
