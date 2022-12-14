# write a recursive function  to calculate the sum of first n natural numbers
##################  method 1
def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)
n = 5
print(recurSum(n))

###############     method 2
def recurSum(n):
    if n<=1:
        return n
    return n + recurSum(n-1)
print(recurSum(5))         