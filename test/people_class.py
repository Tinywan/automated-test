#!/usr/bin/python3

class Person:
    #定义基本属性
    name = ''
    age = 18
    __weight = 100

    #定义构造方法
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        return self.__weight


per = Person('Tinywan',10,30)
print(per)
print(per.name)
print(per.age)
print(per.speak())