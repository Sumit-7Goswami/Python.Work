## Write a program to create a function using following conditions

# It should accept employer name and salary and display both
# if the salary is missing then assign the default value as 10000 to salary
# Ben(12000) # mike(15000) #bob()

def name_salary(name,salary):
    print("name:"+name)
    print("salary:",salary)
    
name_salary("ben",12000)   
name_salary("mike",15000) 
name_salary("bob",10000)






##*** notes**keyword variable length argument

def details(name,*data ):
    print(data)

details("Sumit","Rajasthan",19,999999999)


####
def details(name,*data ):
    print(name)
    for i,j in data.items():
        print(i,j)

details("sumit", place="rajasthan",age=26,no=999999999)    

####
a=10

def func():
    a = 15
    print(a)

func()
print(a)


#####
def hello():
    print("Hello World")
    hello()
'''here print hello world infinite,beacuse we put function into function '''




####  RECURSION
import sys
print(sys.setrecursionlimit())
def hello():
    print("Hello World")
    hello()   

## Recursion
'''haaving a end condition first of all'''  

def sum_recursion(num):
    if num==0:
        return num
    return num+sum_recursion(num-1)    

##factorial
def sum_recursion(num):
    if num==0:
        return num
    return num+sum_recursion(num-1)

ans = sum_recursion(5)
print(ans)





