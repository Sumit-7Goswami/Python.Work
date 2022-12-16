with open("new_04.txt") as f:
    content = f.read()

content = content.replace("don" , "###$%#$@#@$#")

with open("another_04.txt" , "w") as f:
    content = f.write(content)



