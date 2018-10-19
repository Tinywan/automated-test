#!user/bin/python
# coding:utf-8

from selenium import webdriver
import time
import os
if 'HTTP_PROXY' in os.environ:
    del os.environ['HTTP_PROXY']

driver = webdriver.Chrome()
# driver.set_window_size(1024, 500)
# driver.get('https://www.tinywan.com/')
# time.sleep(3)
# print("browser will be closed")
# driver.close()
# print("browser is closed")

# -------restart open
time.sleep(3)
url = 'https://www.tinywan.com/'
print "now access %s" % (url)
driver.get(url)
print "title of current page is %s" % (driver.title)
print "url of current page is %s" % (driver.current_url)
time.sleep(2)
driver.quit()
