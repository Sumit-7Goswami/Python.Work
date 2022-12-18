# DRY--> Don't repeat yourself 

  

class RailwayForm:
    formType = "RailwayForm" 
    def printData(self):
        print(f"name is {self.name}") 
        print(f"Train is {self.train}") 

sumitApplication = RailwayForm()
sumitApplication.name = "Sumit"
sumitApplication.train = "Rajdhani Express" 
sumitApplication.printData()       
