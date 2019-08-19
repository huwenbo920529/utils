#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time    : 2019/8/19 17:32 
# @Author  : Wenbo Hu 
# @Site    :  
# @File    : loggerDemo2.py 
# @Software: PyCharm Community Edition
import logging

# http://blog.csdn.net/zyz511919766/article/details/25136485

# ***************************************************************************************************8
# 默认情况下python的logging模块将日志打印到了标准输出中，
# 且只显示了大于等于WARNING级别的日志，
# 这说明默认的日志级别设置为WARNING
# （日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET），
# 默认的日志格式为   日志级别：Logger名称：用户输出消息

print(logging.critical("critical"))
print(logging.error("error"))
print(logging.warning("warning"))
print(logging.info("info"))
print(logging.debug("debug"))

# ***************************************************************************************************8
# 灵活配置日志级别，日志格式，输出位置
# logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
# filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
# filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
# format：指定handler使用的日志显示格式。
# datefmt：指定日期时间格式。
# level：设置rootlogger（后边会讲解具体概念）的日志级别
# stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
#
# format参数中可能用到的格式化串：
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/test.log',
                    filemode='w')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

# ***************************************************************************************************8
# 若要对logging进行更多灵活的控制有必要了解一下Logger，Handler，Formatter，Filter的概念
# 上述几个例子中我们了解到了logging.debug()、logging.info()、logging.warning()、logging.error()、logging.critical()
# （分别用以记录不同级别的日志信息），logging.basicConfig()
# （用默认日志格式（Formatter）为日志系统建立一个默认的流处理器（StreamHandler），
# 设置基础配置（如日志级别等）并加到root logger（根Logger）中）这几个logging模块级别的函数，
# 另外还有一个模块级别的函数是logging.getLogger([name])（返回一个logger对象，
# 如果没有指定名字将返回root logger）
# 创建一个logger
logger = logging.getLogger()

logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO)

logger3 = logging.getLogger('mylogger.child1')
logger3.setLevel(logging.WARNING)

logger4 = logging.getLogger('mylogger.child1.child2')
logger4.setLevel(logging.DEBUG)

logger5 = logging.getLogger('mylogger.child1.child2.child3')
logger5.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('/test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

# 定义handler的输出格式formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 定义一个filter
# filter = logging.Filter('mylogger.child1.child2')
# fh.addFilter(filter)

# 给logger添加handler
# logger.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)

# logger1.addFilter(filter)
logger1.addHandler(fh)
logger1.addHandler(ch)

logger2.addHandler(fh)
logger2.addHandler(ch)

# logger3.addFilter(filter)
logger3.addHandler(fh)
logger3.addHandler(ch)

# logger4.addFilter(filter)
logger4.addHandler(fh)
logger4.addHandler(ch)

logger5.addHandler(fh)
logger5.addHandler(ch)

# 记录一条日志
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')

logger3.debug('logger3 debug message')
logger3.info('logger3 info message')
logger3.warning('logger3 warning message')
logger3.error('logger3 error message')
logger3.critical('logger3 critical message')

logger4.debug('logger4 debug message')
logger4.info('logger4 info message')
logger4.warning('logger4 warning message')
logger4.error('logger4 error message')
logger4.critical('logger4 critical message')

logger5.debug('logger5 debug message')
logger5.info('logger5 info message')
logger5.warning('logger5 warning message')
logger5.error('logger5 error message')
logger5.critical('logger5 critical message')

# logging库提供了多个组件：Logger、Handler、Filter、Formatter。
# Logger对象提供应用程序可直接使用的接口，Handler发送日志到适当的目的地，
# Filter提供了过滤日志信息的方法，Formatter指定日志显示格式。
# Logger是一个树形层级结构，输出信息之前都要获得一个Logger（如果没有显示的获取则自动创建并使用root Logger，如第一个例子所示）。
# logger = logging.getLogger()返回一个默认的Logger也即root Logger，并应用默认的日志级别、Handler和Formatter设置。
# 当然也可以通过Logger.setLevel(lel)指定最低的日志级别，可用的日志级别有logging.DEBUG、logging.INFO、logging.WARNING、logging.ERROR、logging.CRITICAL。
# Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()输出不同级别的日志，只有日志等级大于或等于设置的日志级别的日志才会被输出。
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)
logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO)
