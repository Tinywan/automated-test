#!/usr/bin/python3

# *------------------------------------------------------------
# |  Author: Tinywan(ShaoBo Wan)
# |  DateTime: 2018/12/4 14:20
# |  Mail: 756684177@qq.com
# |  Desc: 如何使用 from log import logger
# *-------------------------------------------------------------*/

import logging
# logging.handlers.RotatingFileHandler 必须引入才可以使用
from logging import handlers
import os
import sys
import time

class logger:
    def __init__(self, set_level="debug",
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 log_name=time.strftime("%Y-%m-%d.log", time.localtime()),
                 log_path=os.path.abspath(os.path.join(os.path.dirname(
                     os.path.dirname(__file__)), "../logs")),
                 use_console=True):
        '''
            set_level： 设置日志的打印级别，默认为DEBUG
            name： 日志中将会打印的name，默认为运行程序的name
            log_name： 日志文件的名字，默认为当前时间（年-月-日.log）
            log_path： 日志文件夹的路径，默认为logger.py同级目录中的log文件夹
            use_console： 是否在控制台打印，默认为True
        '''
        self.logger = logging.getLogger(name)
        if set_level.lower() == "critical":
            self.logger.setLevel(logging.CRITICAL)
        elif set_level.lower() == "error":
            self.logger.setLevel(logging.ERROR)
        elif set_level.lower() == "warning":
            self.logger.setLevel(logging.WARNING)
        elif set_level.lower() == "info":
            self.logger.setLevel(logging.INFO)
        elif set_level.lower() == "debug":
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.NOTSET)
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_file_path = os.path.join(log_path, log_name)
        log_handler = logging.handlers.RotatingFileHandler(
            log_file_path, mode='a', maxBytes=200, backupCount=0, encoding='utf-8', delay=0)
        log_handler.setFormatter(logging.Formatter(
            "[%(asctime)s]-[%(levelname)s] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] - %(message)s"))
        self.logger.addHandler(log_handler)
        if use_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(
                "[%(asctime)s]-[%(levelname)s] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] - %(message)s"))
            self.logger.addHandler(console_handler)

    def addHandler(self, hdlr):
        self.logger.addHandler(hdlr)

    def removeHandler(self, hdlr):
        self.logger.removeHandler(hdlr)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)

    def file_path(self):
        print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
        print(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "../logs")))   
