#!/usr/bin/python3
from tinydb import TinyDB, Query
db = TinyDB("db.json")
# 返回当前插入的条数
db.insert({'type': 'apple', 'count': 7})
res = db.insert({'type': 'apple', 'count': 9})
print(db.all())
