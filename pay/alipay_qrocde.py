#!/usr/bin/python3

from selenium import webdriver 
from time import sleep
driver = webdriver.Chrome()
driver.get('https://cpay.hypayde.com/t_q_code?id=T10251812171057414120')
sleep(2)
driver.get_screenshot_as_file("D:/aaac.png") # 截图存放路径，使用jpg报错png格式可以
sleep(3)
driver.quit()