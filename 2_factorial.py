#2. Write a python program to calculate the factorial of a number

## Define a function that will be called recursively
def factorialOf(n):
    if (n==0 or n==1):
        return 1
    else:
        return(n * factorialOf(n-1))

##main program
num = int(input("Enter a number for the factorial function:"))
fact = factorialOf(num)
print("Factorial of " + str(num) + " = " + str(fact))