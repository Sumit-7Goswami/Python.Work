# Calculate and print the volume of sphere upto 2 decimal places with the user specified dimension(radius of the sphere) 
#  
# ***volume of the cylinder is 4/3*pi*r***3 

from math import pi
r = int(input("r:"))
vol = (4/3)*(pi)*(r**3)
print(vol)

##  **** see in question wee have to find 2 decimal places so wee will change code
## ex--> x=3.143667 (round this number with 2 decimal places)
'''print(round(x,2))''' # 2 is precision

# if without precision,let see below
x = 3.143667
print(round(x))  
'''we got 3 , the nearest integer we get'''

x = 3.74234
print(round(x))
'''we get 4 , the nearest integer ,if we not mentioned precision'''

x = 1324.81824732
print(round(x, 2)) 

x =1324.81424732
print(round(x, 2))

'''soo this are 1st method to do decimal for float , so many
methoda are there , uu can use any '''

#come on the question again

from math import pi
r = int(input("r:"))
vol = (4/3)*(pi)*(r**3)
print(round(vol, 2))

