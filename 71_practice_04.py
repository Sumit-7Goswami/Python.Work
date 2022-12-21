# write a recursive function  to calculate the sum of first n natural numbers
##################  method 1
num = int(input())
def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)
print(recurSum(num))

###############     method 2
# def recurSum(n):
#     if n<=1:
#         return n
#     return n + recurSum(n-1)
# print(recurSum(5))         