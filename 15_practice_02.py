#Question2--->write a program to fill in a letter template 
#     given below with name and date . 
#
#           letter = ''' Dear <|name|>
#                         you are selected !
#                           <|DATE|> '''

letter = '''Dear <|NAME|>,
Greeting from ABC coding house . I am happy to tell you about your selection 
You are selected!
Have a great day ahead!


Date <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)  
print(letter)


#*******here when i written all the letter in name small ,our code will run but can't call my name 
'''in line 8 , we should write |NAME| then only our name is come in code ,if we write |Name| then 
code will work , but our name will not shown in the code  '''
