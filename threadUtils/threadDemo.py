#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 15:34 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : threadUtils.py 
# @Software: PyCharm Community Edition
import threading


class MyThread(threading.Thread):
    def __init__(self, func, logger, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.logger = logger
        self.result = None

    def run(self):
        self.result = self.func(self.args)

    def get_result(self):
        try:
            return self.result
        except Exception as e:
            self.logger.error("get thread result error, the exception is :{}".format(e))
            return None


def multi_threads(logger, data, thread_func, result_func, thread_params, result_func_params, batch_flag=False):
    """

    :param logger:
    :param data: 要处理的数据
    :param thread_func: 线程调用的函数
    :param result_func: 结果数据处理函数
    :param thread_params: 线程调用的函数的参数
    :param result_func_params: 结果数据处理函数的额外参数
    :param batch_flag:结果数据批处理还是一条条处理
    :return:
    """
    thread_num = 32
    thread_pool = []
    thread_result = []
    if not data:
        logger.error("data is None!")
        return []

    data_len = len(data)
    batch_num = data_len / thread_num
    logger.info("data_len:{}, batch_num:{}".format(data_len, batch_num))
    # 若数据量大于线程池的容量，则每次取线程池容量大小的数据进行处理
    if batch_num >= 1:
        for k in range(batch_num):
            for j in range(thread_num):
                # thread_func函数的第一个参数是loan_id
                thread_param_dict = {"item_data": data[k * thread_num + j], "data_index": k * thread_num + j}
                # thread_param_dict.update({"data_index": k * thread_num + j})
                thread_param_dict.update(thread_params)
                t = MyThread(thread_func, logger, thread_param_dict)
                thread_pool.append(t)
                t.start()
            for t in thread_pool:
                t.join()
                # 将每个线程处理的结果放在线程结果列表中
                if t.get_result():
                    thread_result.append(t.get_result())

            if result_func:
                if not batch_flag:
                    for item in thread_result:
                        # 处理该批线程池返回的结果数据
                        if item:
                            result_func_params_dict = {"thread_result_item": item}
                            result_func_params_dict.update(result_func_params)
                            result_func(result_func_params_dict)
                else:
                    result_func_params_dict = {"thread_result": thread_result}
                    result_func_params_dict.update(result_func_params)
                    result_func(result_func_params_dict)
            # 释放线程池，清空记录
            thread_result = []
            thread_pool = []

    # 当数据小于线程池的容量或最后一部分不足线程池容量的数据
    for j in range(data_len % thread_num):
        thread_param_dict = {"item_data": data[batch_num * thread_num + j], "data_index": batch_num * thread_num + j}
        thread_param_dict.update(thread_params)
        t = MyThread(thread_func, logger, thread_param_dict)
        thread_pool.append(t)
        t.start()
    for t in thread_pool:
        t.join()
        if t.get_result():
            thread_result.append(t.get_result())

    if result_func:
        if not batch_flag:
            for item in thread_result:
                if item:
                    result_func_params_dict = {"thread_result_item": item}
                    result_func_params_dict.update(result_func_params)
                    result_func(result_func_params_dict)
        else:
            result_func_params_dict = {"thread_result": thread_result}
            result_func_params_dict.update(result_func_params)
            result_func(result_func_params_dict)
    # # 释放线程池，清空记录
    # thread_result = []
    # thread_pool = []
