# Tree traversal in Python


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item
        
def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)

def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')

def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(23)
root.left = Node(5)
root.right = Node(56)
root.left.left = Node(34)
root.left.right = Node(22)
root.right.left = Node(12)
root.right.right= Node(18)

print("Inorder traversal ")
inorder(root)
print("\nPreorder traversal ")
preorder(root)
print("\nPostorder traversal ")
postorder(root)









