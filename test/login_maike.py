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

url = 'https://passpt.maike51.com/'
screenImg = "D:/Git/automated-test/images/11001.png"

if 'HTTP_PROXY'in os.environ:
    del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
dr.maximize_window()
dr.get(url)

# account and password
dr.find_element_by_name("account").clear()
dr.find_element_by_name("account").send_keys('11111')
dr.find_element_by_name("password").clear()
dr.find_element_by_name("password").send_keys('111')
dr.find_element_by_id("login-button").click()
dr.quit()
