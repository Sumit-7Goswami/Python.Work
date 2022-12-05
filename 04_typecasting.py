
#typecasting- it is a way to convert one data type to another.

a = "710" #now this is not a integer , because it comes in inverted coloumns
# so it is a string only 
a = int(a)
print(type(a))
print(a + 10 )
'''so after running the code we got 720 and if we take a = "720shdh" here
after runnning the code, we got an error ...
because it cannot convert into integer ..like see below the example '''
 
a = "720shdb"
a = int(a)
print(type(a))
'''run this code and see the result as we got an eeror '''