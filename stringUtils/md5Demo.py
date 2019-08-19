#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 16:40 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : md5Demo.py 
# @Software: PyCharm Community Edition
from hashlib import md5


def md5encode(text):
    if text:
        m = md5()
        m.update(text)
        res = m.hexdigest()
        return res
    else:
        return None
