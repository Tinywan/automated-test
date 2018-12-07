#!/usr/bin/python3

import requests
import json

response = requests.get("http://httpbin.org/get")
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json())) # 其实就是执行了json.loads()方法

# 文件上传
# files= {"files":open(r"D:\Git\automated-test\lib\requests\3.png","rb")}
# response = requests.post("http://httpbin.org/post",files=files)
# print(response.text)


# 获取cookie
response = requests.get("http://www.baidu.com")
# print(response.cookies)

for key,value in response.cookies.items():
    print(key+"="+value)

response = requests.get("https://www.12306.cn",verify=False)
print(response.status_code)    


try:
    response = requests.get("http://httpbin.org/get",timout=0.1)
    print(response.status_code)
except TimeoutError:
    print("timeout")
except ConnectionError:
    print("connection Error")
except Exception:
    print("error")