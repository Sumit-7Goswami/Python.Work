# Write a program to find out whether a given post is talking about " Sumit" or not.

post = input("Enter the post")
if ("SUMIT" in post):
    print("Yes! the post contains the name  sumit ")
elif ("Sumit" in post):
    print("Yes! the post contains the name  sumit")
elif ("sumit" in post):
    print("yes! te post contains the name sumit" )
elif ("SuMit" in post):
    print("Yes! the post contains the name sumit")

else:
    print("No, the post does not contain the name sumit")    
        
     
