# add a static method in problem 2 to greet the user with hello 
# Write a class Calculator capable of finding square , cube and squareroot of a number

class Calculator:
    def __init__(self,num):
        self.number = num

    @staticmethod
    def greet():
        print("Hello Friends")    

    def square(self):
        print(f" The value of {self.number} square is {self.number**2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root  is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

a = Calculator(3)
a.greet()
a.square()                       
a.squareRoot()
a.cube()