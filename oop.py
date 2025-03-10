#OOP: class and object in PYTHON

#example1:student class
#CLASS

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade 
    def get_info(self):
        return f"Name is {self.name} and grade is {self.grade}"
    def is_passed(self):
        if self.grade >= 60:
             return True
        else:
             return False
        
#OBJECT


s1 = Student(name = "GOPAL", grade = 88)
s2 = Student(name = "RAM", grade = 95)
s3 = Student(name = "MAHESH", grade = 20)

print(s1.get_info())
print(s2.get_info())
print(s3.get_info())

print(s1.is_passed())
print(s2.is_passed())
print(s3.is_passed())


