#!/usr/bin/python3

import requests

response = requests.get("https://www.baidu.com")
print(type(response)) # <class 'requests.models.Response'>
print(response.status_code) #  200
print(type(response.text)) # <class 'str'>
# print(response.text)
# print(response.cookies)
# print(response.content)
# print(response.content.decode("utf-8"))
response.encoding="utf-8"
print(response.text)

# get
data = {
    "name":"zhaofan",
    "age":22
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.url) # http://httpbin.org/get?name=zhaofan&age=22
print(response.text)