def hello():
    print("HELLO WORLD")

def hello_mars():    
    print("Hello Mars")


hello_mars()     # here print Hello Mars

####
def name(x):
    print(x)

name(4)   # this will print 4 


###
def add(num1,num2):
    sum = num1 + num2
    print(sum)

add(5,10)
add(14,51)
add(74,42)
add(16,21)


##
def diff(num1,num2):
    diff = num1-num2
    print(diff)

diff(14,7)
diff(17,21)


### orr we can also get output without writting print
def add(num1,num2):
    sum = num1 + num2
    return sum

add(1,2)
add(12,24) # see this is the real meaning of using def

#####
def add(num1,num2):
    sum = num1 + num2
    return sum

result = add(1,4)
print(result)


