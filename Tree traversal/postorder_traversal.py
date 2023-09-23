class Node:
    def __init__(self,v,left=None,right=None) -> None:
        self.value=v
        self.left=left
        self.right=right

'''
Postorder Traversal

it follows the Left-Right-Root policy such that for each node:

- The left subtree is traversed first
- Then the right subtree is traversed
- Finally, the root node of the subtree is traversed

'''


# using Recursion
def postorder_recursion(node):
    if node is None:
        return []
    left = postorder_recursion(node.left)
    right =postorder_recursion(node.right)

    return left + right+[node.value]
# using iterative
def postorder_iterative(root):
    if root is None:
        return []
    res=[]
    stack=[root]
    
    while(len(stack)>0):
        node = stack.pop()
        res.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]




        
# Creating BST
def array_to_bst(arr):
    if not arr:
        return None
    
    mid= len(arr)//2
    root= Node(arr[mid])

    root.left = array_to_bst(arr[:mid])
    root.right = array_to_bst(arr[mid+1:])

    return root


sorted_array=[1,2,3,4,5,6,7]
# creating BST form array
root = array_to_bst(sorted_array)
print("Postorder traversal")
a=postorder_recursion(root)
print(f"using Rescursion {a}")
b = postorder_iterative(root)
print(f"using iterative {b}")