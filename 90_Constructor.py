class Employee:
    company = "Google"

    def __init__(self , name , salary , subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")  
        print(f"The salary o the employee is {self.salary}")  
        print(f"The subunit of the employee working in {self.subunit}")

        def getSalary(self , signature):
            print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")


        @staticmethod    
        def greet():
            print("Good Mrg sir")

        @staticmethod
        def time():
            print("The time is 9 Am in the morning")

Sumit = Employee("Sam",10000,"yt")    
# Sumit = Employee() ..here we got error ,because we give two arguments
Sumit.getDetails()        

