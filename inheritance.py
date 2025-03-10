#inheritance
#base class and derived class


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    def get_info(self):
        print(f"Name  is {self.name}, Age is {self.age }")


class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade =  grade

    def get_info(self):
        super().get_info()
        print(f"Grade is {self.grade}" )



s1 = Student(name = "Gopal", age=  30, grade = 14)

s2 = Student(name = "Dhan", age = 24,  grade = 15)

s1.get_info()



