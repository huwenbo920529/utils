#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 17:00 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : reflectionDemo.py 
# @Software: PyCharm Community Edition


def func1(a1, b1):
    c1 = a1 + b1
    print("hello1, {}".format(c1))


def func2(a2, b2):
    c2 = a2 + b2
    print("hello2, {}".format(c2))


def func_reflect(argument):
    switcher = {
        "01": func1,
        "02": func2,
    }
    return switcher.get(argument)


if __name__ == '__main__':
    func_reflect("01")(1, 2)
