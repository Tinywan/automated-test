#from 模块 import 方法变量

# 方式一 同级目录
# import c1
# print(c1.mobile)

# from c1 import mobile
# print(mobile)

# 方式二 不同级目录
# import lib.audio
# print(lib.audio.desc)

# from lib.audio import desc
# print(desc)

# import lib.audio as a
# print(a.desc)
# print(a.flv)

# 方式三 不同级目录
# from lib.audio import *
# print(flv) # ok
# print(desc) # error

# from lib.audio import (flv,mp4,hls)

import lib 
# 默认执行初始化文件 This is __init__.py file

