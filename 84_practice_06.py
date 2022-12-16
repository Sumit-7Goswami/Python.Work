# write a program to make a copy of a text file "poem.txt"
with open("poem.txt") as f:
    content = f.read()

with open("copy.txt","w") as f:
    f.write(content)    