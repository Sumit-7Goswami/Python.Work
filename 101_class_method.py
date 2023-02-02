# A class method is a method which is bound to the class and not the object of the class .
# #    @classmethod is used to create a class method 

#syntax to create a class method 
#   @classmethod
#   def(cls , p1 , p2):
 

class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self , sal):
    #     self.salary = sal

    # def changeSalary(self,sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls , sal):
        cls.salary = sal


e = Employee()
print(e.salary)

e.changeSalary(455)
print(e.salary)
print(Employee.salary)