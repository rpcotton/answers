#3. Write python code to remove duplicates from a list

##main program
# Get user input and split it into a list
inputlist = input("Enter list of numbers separated by space: ").split()
print("List provided:", inputlist)

# Use set function to eliminate duplicates within the list
uniqlist = set(inputlist)
print("Removing duplicates from the list : ")
print(uniqlist)