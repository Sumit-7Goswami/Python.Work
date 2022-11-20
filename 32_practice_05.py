
# QUESTION 5 --> Create an empty dictionary .Allow 4 friends to enter their favourite
#  language as values and use keys  as their names . Assumes that the names
#   are unique .  

favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n ")
d = input("Enter your favorite language Harshita\n")
favLang['Shubham'] = a
favLang['ankit']   = b
favLang['sonali']  = c 
favLang['harshita'] = d 

print(favLang)



'''related question to above question'''
# QUESTION 6---> If language of 2 friends are same ; What will to the program in problem 5 

favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n ")
d = input("Enter your favorite language Harshita\n")
favLang['Shubham'] = a
favLang['ankit']   = b
favLang['Shubham']  = c 
favLang['harshita'] = d 

print(favLang) 



# question----> # QUESTION 6---> If language of 2 friends are same ; What will to the program in problem 5 

