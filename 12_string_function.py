story = "Once upon a time there was a youtuber named Harry who  uploaded python with notes"

#string functions
print(len(story))     
''' here len means lenth of words in story,there is 81 words so answer 
is 81...like len("Harry")-----> returns 5 '''

print(story.endswith("python"))  
'''here we got false because story not ends with python ,the story ends with '''

print(story.endswith("notes")) 
'''now we get true on run this code '''

print(story.count("a"))  
'''here are total 6 'a' letter in the story '''

#capitalize--->>>> first word will convert into capital 
print(story.capitalize()) 
'''once mai o small krr kk run krna ..capital bna dega '''

print(story.find("Harry"))

print(story.find("hary"))
'''if we run this code , we get -1 ..its means there is not word exist '''

story = "Once upon a time there was a youtuber named Harry who  uploaded python with notes"
print(story.find("Once"))

story = "Once upon a time there was a youtuber named Harry who  uploaded python upon notes"
print(story.find("upon"))
'''so here you see what i did i add 'upon' word 2 times in story and here we should
know that only 1st upon or 1st word of similiar words only exist not other '''

story = "Once upon a time there was a youtuber named Harry who  uploaded python with notes"
print(story.replace("Harry", "CodeWithHarry"))

