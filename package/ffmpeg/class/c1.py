
class Student():
    name = "default"
    age = 24
    sum = 100

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print(self.__class__.sum)

    def getInfo(self):
        print("name "+self.name)
        print("age "+str(self.age))

# stud1 = Student()
# stud2 = Student()
# stud3 = Student()
# # stud1.getInfo()

# print(id(stud1)) # 2825425418392
# print(id(stud2)) # 2825425418560
# print(id(stud3)) # 2825425418728

# stud1 = Student()
# stud1.__init__()

