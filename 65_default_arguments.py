# default arguments
'''we can have a value as default arguments in a function.
If we specify name = "stranger" in the line containing def , this value is used when no arguments are passed. 
'''

def greet(name):
    print("Goood Day "+ name)

greet("Sumit")
greet()  ### like if we run this code ,it will tell one argument is misssing , for that we use "default arguments" ,,,,like see this below example


def greet(name="stranger"):
    print("Good day "+ name)    #we can also use return here instead of using print

greet("Sumit")
greet()
 


