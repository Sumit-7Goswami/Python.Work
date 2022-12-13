# QUESTION ---> print the factorial of n number 

n = 5
product = 1
for i in range(n):
    product = product * (i+1)
print(product)        

### function iterate
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return product

print(factorial_iter(6))
print(factorial_iter(4))        



