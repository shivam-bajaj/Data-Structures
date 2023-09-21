class Node:
    def __init__(self,v,left=None,right=None) -> None:
        self.value=v
        self.left=left
        self.right=right

'''
Inorder traversal
Technique follows the Left-Root-Right pattern.
- The left subtree is traversed first
- Then the root node for that subtree is traversed
- Finally, the right subtree is traversed

Two approaches:
1. using Recurison
2. using Iterative
'''



# Using Recurision
def inorder_traversal_recursion(node):

    if node is None:
        return []
    
    left_values= inorder_traversal_recursion(node.left)
    right_values = inorder_traversal_recursion(node.right)

    return left_values + [node.value] + right_values


# Using Iterative approach
def inorder_traversal_iterative(root):
    if root is None:
        return None
    
    res=[] 
    stack=[]
    temp=root
    while(len(stack)!=0 or temp!=None):
        if temp is not None:
            stack.append(temp)
            temp=temp.left
        else:
            temp=stack.pop()
            res.append(temp.value)
            temp=temp.right
    return res



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

print("Inorder Traversal")

a=inorder_traversal_recursion(root)
print(f"using recurion: {a}")

b = inorder_traversal_iterative(root)
print(f'using iterative: {b}')

