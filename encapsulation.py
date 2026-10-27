class Student:
    def __init__(self, r,n, m, email):
        self.__roll = r
        self.__name = n
        self.__marks = m
        self.__email = email

    def set_roll(self, nr):
        self.__roll = nr

    def getRoll(self):
        return self.__roll
    
    def set_name(self , nn):
        self.__name = nn

    def getname(self):
        return self.__name

    def setmarks(self):
        self.__marks = m

    def getmarks(self):
        return self.__marks
    
    def setemail(self):
        self.__email = email

    def getemail(self):
        return self.__email

s1 = Student(1 , "jay", 57, "jay@gmail.com")
s1.set_roll(4)

res1 = s1.getRoll()

res2 = s1.getname()
res3 = s1.getmarks()
res4 = s1.getemail()

print( res1)
print(res2)
print(res3)
print(res4)