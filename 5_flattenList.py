#5. Write a python code to implement a function to flatten a nested list

#define recursive function to flatten nested list
def reemovNesting(l):
    for i in l:
        if type(i) == list:
            reemovNesting(i)
        else:
            output.append(i)

#main program

# input list
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#l = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
output = []
print('The original list: ', l)
reemovNesting(l)
print('The list after removing nesting: ', output)
