#!/usr/bin/python3

from time import sleep
# a = 1.1
# print(a)
# print(isinstance(a,int))

# a,b,c = 1,True,1.2
# print(a)
# print(b)
# print(c)

# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
# complexList = list + tinylist*3
# print(list)
# print(tinylist)
# print(complexList)

# tupleStr = (1,2,3,4)
# print(tupleStr)
# print(id(a))

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

if "Tinywan" in student:
    print("OK")
else:
    print("fail")    

 
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
 
# print(a)
 
# print(a - b)     # a 和 b 的差集
# print(a | b)     # a 和 b 的并集
# print(a & b)     # a 和 b 的交集
# print(a ^ b)     # a 和 b 中不同时存在的元素

# a = {}
# a['name'] = 'Tinywan'
# a['age'] = 24
# print(a)
# print(a.keys())
# print(a.values())

'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''

print("I name %s age is %d" % ("Tinywna",24))

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

a,b = 0,1
while b<10:
    print(b ,end=',')
    a , b = b,a+ b

n = 100
sum = 0
counter = 1

while counter < n:
    sum = sum + counter
    counter +=1
print("1 到 %d 之和为: %d" % (n,sum))

languages = ["C", "C++", "Perl", "Python"] 
for language in languages:
    print(language)


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

str = input("请输入：")
print ("你输入的内容是: ", str)

# 打开一个文件
f = open(".\\foo.txt", "w")

f.write( str )

# 关闭打开的文件
f.close()

try:
    f = open('foo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
  