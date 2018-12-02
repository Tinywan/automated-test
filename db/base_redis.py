#!/usr/bin/python3

import redis
# 创建redis链接对象
r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
# 存储键值对
r.set('site', 'www.tinywan.com')
# 获取值
print(r.get('site'))
