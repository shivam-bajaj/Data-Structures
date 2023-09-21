class Node:
    def __init__(self,v,left=None,right=None) -> None:
        self.value=v
        self.left=left
        self.right=right


# Creating BST
def array_to_bst(arr):
    if not arr:
        return None
    
    mid= len(arr)//2
    root= Node(arr[mid])

    root.left = array_to_bst(arr[:mid])
    root.right = array_to_bst(arr[mid+1:])

    return root

# inorder Traversal
def inorder_traversal(node):

    if node is None:
        return []
    
    left_values= inorder_traversal(node.left)
    right_values = inorder_traversal(node.right)

    return left_values + [node.value] + right_values

arr = [7,4,3,5,2,6,1]
root = array_to_bst(sorted(arr))

a = inorder_traversal(root)
print(f"Inorder traversal: {a}")
