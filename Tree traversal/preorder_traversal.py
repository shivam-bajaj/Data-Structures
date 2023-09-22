class Node:
    def __init__(self,v,left=None,right=None) -> None:
        self.value=v
        self.left=left
        self.right=right

'''
Preorder Traversal
It follows the Root-Left-Right policy where:

- The root node of the subtree is visited first.
- Then the left subtree  is traversed.
- At last, the right subtree is traversed.

'''



# using recursion
def preorder_recurison(node):
    if node is None:
        return []
    left_values = preorder_recurison(node.left)
    right_values= preorder_recurison(node.right)

    return [node.value]+left_values+right_values        




# using iterative
def preorder_iterative(root):
    if root is None:
        return []
    res=[]
    stack=[root]
    while (len(stack)>0):
        node=stack.pop()
        res.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

# another iterative approach
def preorder(root):
    res=[]
    stack=[]
    temp=root
    while(temp or stack):
        if temp is not None:
            res.append(temp.value)
            if temp.right:
                stack.append(temp)
            temp=temp.left
        else:
            temp = stack.pop()
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

print("Preorder Travesal")

b=preorder_recurison(root)
print(f"using recursion: {b}")

a=preorder_iterative(root)
print(f"using iterative: {a}")

c = preorder(root)
print(f"using another iterative approach: {c}")