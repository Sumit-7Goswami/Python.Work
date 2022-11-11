# write a program to print multiplication table of a given number using for loop
num = int(input("Enter the number"))
for i in range(0 ,11):
    print(str(num) + " * " + str(i) + "=" + str(i*num))



#trick--- f string ---> f string kya hai..bss ye zindagi ko asssann bnata hai'''
num = int(input("Enter the number"))
for i in range(1 , 11):
    print(f"{num}*{i}={num*i}") 
'''if we run this code then also our code exists ...you can check this running in other pages'''    



