#4. Write a python code to find the first non repeating character in a string

def firstnonrepeatingchar(inputStr):
    for char in inputStr:
        if inputStr.count(char) == 1:
            print(f"The first non repeating character in the strings is {char}")
            return
    print("There is no non repeating character in the string provided")

##main program
# Get user input string
inputstring = input("Enter a string: ")
firstchar = firstnonrepeatingchar(inputstring)
