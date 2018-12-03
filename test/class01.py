#!/usr/bin/python3

class MyClass(object):
    """一个简单的类实例"""
    i = 111
    def name(self):
        return "Tinywan Name"

# 实例化类
# x = MyClass()

# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.name())  

# class ComplexClass():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# x = ComplexClass("name", 24)
# print(x.name, x.age)   


# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
 
# t = Test()
# t.prt()

class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)

 
t = Test()
t.prt()

class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private
 
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)
 
    def __foo(self):          # 私有方法
        print('这是私有方法')
 
    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()
 
x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出