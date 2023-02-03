# @property decorators
# consider the following cases
'''class Employee :
        @property
        def name(self):
            return self.ename'''

'''if e=Employee() is an object of class employee , 
we can print(e.name) to print the ename/call name() function'''

'''@getters and @setters'''
'''The method name with @property decoder is called getter method
we can define a function + @name.setter decorator like below : 
        @name.setter
        def name(self.value):
            self.ename = value'''





class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus


    @totalSalary.setter
    def totalSalary(self, val):
        self.salary = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)        
