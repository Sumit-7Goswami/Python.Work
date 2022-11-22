# An empty set can be created using the below syntax
b = set()
print(type(b))


# adding the values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) #adding a value repeteadily does not change set
b.add(5)

print(b) 

#
b = set()
print(type(b))

b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add([4,5,6])

print(b)  
'''we cannot add list in set , because list is not hasable , lekin tupple ko jarur daal skte hai 
..nichee diye hue example ko dyaan se dekho'''


b = set()
print(type(b))

b.add(4)
b.add(4)
b.add(9)
b.add(5)
b.add((1,2,3))  #add tuple 

print(b) 

'''we cannot add dictionaryy  b.add({4:5})   even in sets'''




#
b = set()
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add((4,5,6))

#Length of the set
print(len(b)) #---> prints the length of the set

# after run this code we get answer 3 , because (tuple hai , 4 ,5)


# Removal of an Item
b.remove(5)  
print(b)     # remove 5 from the set 

b.remove(15)
print(b)    #throw an error while trying to remove 15 (which is not present in the list)



## S.pop ---> removes an arbitary elements from the set and returns the element removed

b = set()
b.add(4)
b.add(5)
b.add(2)
b.add((4,5,6))

print(b.pop()) #randomly kisi koi be  remove krr dega 
print(b) 
'''run this code and check 2 is removed from there '''


# S.clear() : empties the set S 
