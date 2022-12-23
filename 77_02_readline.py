f = open('sample.txt')  ## if we not write 'r' ,then it autmotically read ,we call it default
#   read first line 
data = f.readline()
print(data)

#  read 2nd line -
data = f.readline()
print(data)

# Read 3rd line
data = f.readline()
print(data)

# Read fourth line... and soo on
data = f.readline()
print(data)
f.close()


