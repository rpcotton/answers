#1. Write a python program to count the number of vowels in a string

## Define a function
def countvowels(ipstring):
    countv=0
    for char in ipstring:
        if char in "aeiouAEIOU":
           countv += 1
    return countv

##main program
mystr = input("Enter a string:")
count = countvowels(mystr)
print(f"Count of vowels = {count}")