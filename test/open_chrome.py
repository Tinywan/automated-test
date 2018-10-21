#!user/bin/python
# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
url = 'https://pay.hongnaga.com/?debug=true'
print "now access %s" % (url)
driver.get(url)

# 使用switch_to.alert()方法定位到 alert/confirm/prompt
layer = driver.switch_to.alert
layer.send_keys('112233')
# accept。点击确认按钮
layer.accept()

print "title of current page is %s" % (driver.title)
print "url of current page is %s" % (driver.current_url)
# time.sleep(2)

# 下拉框选择
pay_type = Select(driver.find_element_by_id("pay_type"))
driver.find_element_by_id("pay_type").click()
pay_type.select_by_value("13")

# set price text
price = driver.find_element_by_name("price")
# 不清除，则会添加在原来的后面
price.clear()
price.send_keys("0.01")

time.sleep(2)

# 支付按钮
driver.find_element_by_id("pay").click()
# driver.quit()
