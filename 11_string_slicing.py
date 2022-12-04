greeting = "Good Morning,"
name = "Sumit"
#print(type(name))
print(greeting + name)


greeting = "Good Morning,"
name = "Sumit"
#concatenating two strings 
c = greeting + name 
print(c)

# now we talk  about lenth ..like my name is "sumit" ,so here length is 4
# because computer usually start count from 0(zero) number 
# like sumit has S-->0 U-->1 M--->2 I-->3 T--->4 
# so total lenth is 4 
name = "Sumit"
print(name[0])


name = "Sumit"
print(name[1])

name = "Sumit"
print(name[2])

name = "Sumit"
print(name[3])

name = "Sumit"
print(name[4])

''' * * *    name[3] = "d" --------> Does not work'''



########
#######   STRING SLICING 

name = "Sumit"
print(name[0:3])     # '''here [0:3] represent 0,1,2 only not 3 ....if [0:4] then we got 0,1,2,3
                     #  if [1:4] then we get  1,2,3'''


name = "Sumit"
print(name[1:4]) #if we run this code , we get umi of sumit word and 

# print(name[0:4]) = print(name[:4])

print(name[1:]) #is same is name[1:5]  
               

##
######
"Slicing with skip values"
#****we can provide a skip values as a part of our slice like this 
#                   word =  "amazing" 
#                   word [1:6:2] --------->>> '1:6' we get "mazin" and thatn '2' meaning is 
#                                          to skip the second value in "mazin" , then our final 
#                                           answer is   ''' mzn '''  

