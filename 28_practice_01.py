
# Question--> Write a program to create a dictionary of Hindi words with values as their 
#        english translation . Provide user with an option to look it up 
myDict = {
    "Pankha" : "Fan" ,
    "Dabba" : "Box" ,
    "Vastu" : "Item"
}
print("Option are ",myDict.keys())
a = input("Enter the Hindi Word\n")
print("The meaning of your Word is:",myDict[a]) 

#

myDict = {
    "Pankha" :"Fan" ,
    "Dabba" : "Box" ,
    "Vastu" : "Item"
}
print("Option are ",myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is :", myDict[a])

# Below line will not throw an error if the keys is not present in the dictionary
print("The meaning of your word is :", myDict.get[a])

"here the seccond case not throe error it only say none to our code if some word is not in dict.. "
