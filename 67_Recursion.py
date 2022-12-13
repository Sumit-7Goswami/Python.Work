# n! = 1 * 2 * 3 * 4 * 5 *.....n
# n! = n*(n-1)

def factorial_recursive(n):
    if n==1 or n==0:     ## if we don't do this condition ,then the loop will continue infinite
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))
print(factorial_recursive(0))
print(factorial_recursive(1))


#### input method 
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Enter the value n "))
result = factorial(n)    ##   result=res
print(result)            