# write a program to read the text from a given file 'poem.text' and find out whether it contains the word "twinkle"  

f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()        