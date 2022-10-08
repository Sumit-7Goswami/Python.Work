# Question ---> Write a program to detect double spaces in a string    

st = "This is a string with double spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)     
'''here we detect there is no double spaces in string and we got
answer which is -1  '''


#Question---> Replaces the double spaces from Problem 3 with single spaces.
string = "My name is  Mitchell Starch , I  bowl with a speed of 150kmph"
doubleSpaces = string.replace("  "," ") 
print(doubleSpaces)