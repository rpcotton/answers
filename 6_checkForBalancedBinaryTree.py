#6. Write a python program to check if binary tree is balanced

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        
#define recursive function to see if left subtree and right subtree are balanced
def is_balanced_helper(root):
    # a None tree is balanced
    if root is None:
        return 0
    left_height = is_balanced_helper(root.left)
    # if the left subtree is not balanced, then:
    # this tree is also not balanced
    if left_height == -1:
        return -1
    # if the right subtree is not balanced, then:
    # this tree is also not balanced
    right_height = is_balanced_helper(root.right)
    if right_height == -1:
        return -1
    # if the diffrence in heights is greater than 1, then:
    # this tree is not balanced
    if abs(left_height - right_height) > 1:
        return -1
    # this tree is balanced, return its height
    return max(left_height, right_height) + 1
    
def isBalanced(root):
    return is_balanced_helper(root) > -1
    
#main program

# Representation of input Binary tree:
#            1
#           / \
#          2   3
#         /  \
#        4   5 
#       /
#      8

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

print("True" if isBalanced(root) else "False")
