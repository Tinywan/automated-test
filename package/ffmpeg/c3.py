# import lib
# import sys
# from lib import sys
# print(lib.sys.path)
# print(sys.path)
# sys.setrecursionlimit(1000000) # 限制递归

def print_code(skill1,skill2):
    dame1 = skill1 * 2
    dame2 = skill2 * 100
    return dame1,dame2

# dames = print_code(100,300)
# print(type(dames)) # <class 'tuple'> 
# print(dames[0]) # 
# print(dames[1]) # 

skill_dame1 ,skill_dame2 = print_code(10,30)
print(skill_dame1,skill_dame2)

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# 一个变量接受三个值
e = 1,2,3
print(type(e)) # <class 'tuple'>
a,b,c = e
print(a)
print(b)
print(c)

f,g = [11,22,33]
