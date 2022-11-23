# QUESTION -3 -->   Check that a tuple cannot be changed in Python

a = (2,4,6,8,3)
a[0] = 31 
print(a)  



# QUESTION - 4 ---> Write a program to sum a list with 4 numbers.

a = [2,4,56,7]
print(a[0]+a[1]+a[2]+a[3])  #'''or we do like this also   --->   print(sum)''' 


#Question - 5 ---> Write a program to count the number of zero in the following tuple :
#                       a = (7,0,8,0,0,9)

a = (7,0,8,0,0,9)
a.count(0) #no need of writting 18 line ,we can directly do 19 point step ..and get our answer
print(a.count(0)) 