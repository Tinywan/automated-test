#!/usr/bin/python3

from log_pkg import logger

x = logger.logger()

x.critical("这是一个 critical 级别的问题111111111111111！")
x.error("这是一个 error 级别的问题！")
x.warning("这是一个 warning 级别的问题！")
x.info("这是一个 info 级别的问题！")
x.debug("这是一个 debug 级别的问题！")

# import sys
# sys.path.append(r"D:\Git\automated-test")
# import pwcong

# pwcong.hi()


