#Q write a python program to find average of two numbers entered by the
# by the  users .
'''a = input("Enter first number: ")
   b = input("Enter second number: ")
   avg = (a + b)/2 
   print("The average of a and b is", avg) '''

'''we got error on running because 'a' is string ,'b' is string , so its not
make any sense ..for this we convert it into int... see below how we do'''

a = input("Enter first number :" , )
b = input("Enter second number:" ,)
a = int(a)
b = int(b)
avg = (a+b)/2
print("The average of a and b is " , avg )