# Inheritance is a way of creating a new class from an existing class  


# Single inheritance *******************


class Employee:   # parent class   
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):    # class programmer child class hh class employee kii 
    lang = "Python"
    # company = "youtube"  
    def getLanguage(self):
        print(f"The language is {self.language}")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()  
print(p.company)
