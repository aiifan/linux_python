#!/usr/bin/python
#encoding:utf-8

import logging

logging.basicConfig(filename="app.log", level=logging.INFO)    #生成日志文件

"""
Logger:日志记录器，应用程序中能直接使用的接口
Handler：日志处理器，用以表明将日志保存到什么地方以及保存多久
Formmatter:格式化，用以配置日志的输出格式
"""

logging.debug("debug message")  #10  
logging.info("info message")    #20
logging.error("error message")  #40
logging.warn("warn message")    #30
logging.critical("critical message")   #50  严重错误，表明软件已经不能继续运行了