class Remote():
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()


### now we talk about class attributes ,which related to claas only
class Employee:
    company = "Google"

sumit = Employee()    
ash = Employee()
print(sumit.company)    
print(ash.company)
'''if we have to change compant name'''
Employee.company = "Youtube"
print(sumit.company)    
print(ash.company)



######## Instances Attributes
'''An attribute that belongs  to the instance (object) .Assuming the class fom the previous example '''




class Employee:
    company = "Google"
    salary = "55k"

sumit = Employee()    
ash = Employee()

# creating instances attributes salary for both the objects 
# sumit.salary = "30k" 
# ash.salary = "40k" 
print(sumit.company)    
print(ash.company)
'''if we have to change company name'''
# Employee.company = "Youtube"  
# print(sumit.company)    
# print(ash.company)
sumit.salary = "87k"
print(sumit.salary)
print(ash.salary)
'''Instances attributes take preference over class attributes  during assignment and retrieval'''








