# Create a class with a class attribute a ; create an object from it and set a directly using object a = 0 .Does thiw change the class attributes . 
class Sample:
    a = "Sumit"

obj = Sample()
obj.a = "STokes"    

print(Sample.a)
print(obj.a)

## so answer is NO