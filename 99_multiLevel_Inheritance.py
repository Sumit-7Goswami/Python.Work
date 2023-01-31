class Person :
    country = "India"

    def takeBreak(self):
        print("I am breathing.....")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am an employee so I am breathing")  

class Programmer(Employee):
    company = "Fiverrr"

    def getSalary(self):
        print(f"No salary to programers")

p = Person()
p.takeBreak()
# print(p.company)  # throws an error
e = Employee()
print(e.company)
pr = Programmer()
pr.takeBreak()
print(pr.company)
print(pr.country)