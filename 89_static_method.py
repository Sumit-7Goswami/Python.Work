# sometimes zwe need a function that does not use the self parameter we can define a static method like this :
#  @staticmethod

class Employee:
    company = "insta"

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning ,Sir")  

    @staticmethod
    def time():
        print("The time is 9AM")    

Sumit = Employee()
Sumit.salary = 10000
Sumit.getSalary("Thanks")  #Employee.getSalary(Sumit) 
Sumit.time()
Sumit.greet()


