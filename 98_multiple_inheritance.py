# Multiple Inheritance
'''Multiple inheritance occurs when the child class inherits from more than one parent class'''


class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee , Freelancer):
    name = "Sumit"

p = Programmer()    
p.upgradeLevel()
print(p.level)
print(p.company)  # visa will print between visa and fiverr , in line 16 inherit class mm employee phele likha hh aur free lancer baad mm ,,, so it makes first one things to be happen