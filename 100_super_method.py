# Super method is used to access the methods of a super class in the derived class 

#     super().__init__()  <----call constructor of base class 

class Person :
    country = "India"

    def takeBreak(self):
        print("I am breathing.....")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        super().takeBreak()
        print("I am an employee so I am breathing")  

class Programmer(Employee):
    company = "Fiverrr"

    def getSalary(self):
        print(f"No salary to programers")

    def takeBreak(self):
        super().takeBreak()
        print("I am a Programmer so I am breathing++..") 

p = Person()
p.takeBreak()
 
e = Employee()
e.takeBreak()


pr = Programmer()
pr.takeBreak()






###########****************&&^^%%#####
''' now we can use super method to run constructor'''


class Person :
    country = "India"
    
    def __init__(self):
        print("initialising person....\n")

    def takeBreak(self):
        print("I am breathing.....")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initialising employee....\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        super().takeBreak()
        print("I am an employee so I am breathing")  

class Programmer(Employee):
    company = "Fiverrr"

    def getSalary(self):
        print(f"No salary to programers")

    def takeBreak(self):
        super().takeBreak()
        print("I am a Programmer so I am breathing++..") 

# p = Person()
# p.takeBreak()
 
e = Employee()
# e.takeBreak()


# pr = Programmer()
# pr.takeBreak()

