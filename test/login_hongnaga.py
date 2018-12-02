#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import re
import sys
import io
from PIL import Image, ImageEnhance
import pytesseract
from imp import reload

url = 'https://testpay.hongnaga.com/admin/login'
screenImg = "D:/Git/automated-test/images/11001.png"

if 'HTTP_PROXY'in os.environ:
    del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
dr.maximize_window()
dr.get(url)

# account and password
dr.find_element_by_name("username").clear()
dr.find_element_by_name("username").send_keys('admin')
dr.find_element_by_name("password").clear()
dr.find_element_by_name("password").send_keys('12233')

# 验证码处理
imgsrc = dr.find_element_by_id("captcha_img").get_attribute("src")
if re.match(r"https://testpay.hongnaga.com/captcha.html?.*", imgsrc):
    print("Need Validate")
    # 浏览器页面截屏
    dr.get_screenshot_as_file(screenImg)
    # 验证码处理
    location = dr.find_element_by_id('captcha_img').location
    size = dr.find_element_by_id('captcha_img').size
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']  # 1095.0
    bottom = location['y'] + size['height']  # 539.0

    # 从文件读取截图，截取验证码位置再次保存
    img = Image.open(screenImg).crop((left, top, right, bottom))
    img = img.convert('L')  # 转换模式：L | RGB
    img = ImageEnhance.Contrast(img)  # 增强对比度
    img = img.enhance(2.0)  # 增加饱和度
    img.save(screenImg)
    # # 再次读取识别验证码
    img = Image.open(screenImg)
    sleep(1)
    code = pytesseract.image_to_string(img)
    #code= pytesser.image_file_to_string(screenImg)
    dr.find_element_by_name("captcha").clear()
    dr.find_element_by_name("captcha").send_keys(code.strip().replace(' ', ''))
    print(code.strip())
    sleep(1)
else:
    print("Not Need Validate")
dr.find_element_by_id("sub").click()
sleep(10)
dr.quit()
