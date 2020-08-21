import string

def ispangram(sentence):
    return (set(sentence) >= alphabets)# String Comparison

fhandle=open(input("Enter the name of the file:"))

alphabets = set(string.ascii_lowercase)
# set() of alphabets

count=0

for line in fhandle:
    pangram = ispangram(line.rstrip().lower())
    if pangram == True:
        print(" Line "+str(int(count))+" : "+str(line)+" "+"is a Pangram")
    count+=0.5
    print()
       
        
