
## reading the file in python
f = open('sample.txt','r') # by-dafault the mode is 'r'
# data = f.read()
data = f.read(5)
print(data)
f.close()

# f.read(5)  --> then it reads only 5 character
#  f.read()    ---> print the words which is wriiten in files