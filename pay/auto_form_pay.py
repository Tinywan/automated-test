#!/usr/bin/python3
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver_path = ".\chromedriver.exe"
# 支付demo界面
for i in range(1, 100):
    print(i)
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('https://testpay.hongnaga.com/?debug=true')

    # driver.maximize_window()
    a = driver.switch_to.alert
    a.send_keys("123456778")
    # time.sleep(1)
    a.accept()

    driver.implicitly_wait(2)
    pay_type = Select(driver.find_element_by_id("pay_type"))
    driver.find_element_by_id("pay_type").click()
    pay_type.select_by_value("13")
    # time.sleep(3)

    # driver.implicitly_wait(5)
    # driver.find_element_by_link_text("新支付宝转账").click()#支付方式
    # driver.implicitly_wait(5)
    # driver.find_element_by_class_name("form-control").send_keys("0.01")#金额
    # driver.implicitly_wait(5)
    driver.find_element_by_id("pay").click()
