class Student:
    def __init__(self, name=None, age=0):
        self.__name = name          #__가 변수앞에 붙으면 외부에서 변경 불가
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def setName(self,name):
        self.__name = name

stu = Student("Admiral", 25)
print(stu.getName())
print(stu.getAge())

