# self parameter 
'''self refers to the instances of the class .It is automatically passed with a function will from an object'''
#            '''harry.getsalary()
#   here self is harry ,equivalent to employee.getsalary(harry)'''

class Employee:
    company = "insta"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 10000
harry.getSalary()  # Employee.getSalary(harry)