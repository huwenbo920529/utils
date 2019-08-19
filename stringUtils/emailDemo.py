#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 15:55 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : emailDemo.py 
# @Software: PyCharm Community Edition
import re


def is_valid_email_address_format(email_address):
    """
    判断邮箱地址的格式是否正确
    :param email_address:
    :return:
    """
    if not email_address or not isinstance(email_address, str):
        return False
    elif not re.match(".+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email_address):
        return False
    else:
        return True

