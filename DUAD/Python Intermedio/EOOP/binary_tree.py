class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def print_tree(self, node):
        if node is None:
            return
        print(node.value)
        self.print_tree(node.left)
        self.print_tree(node.right)


# --- Tests ---
tree = BinaryTree()

# Construimos el árbol manualmente:
#        1
#       / \
#      2   3
#     / \
#    4   5

tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Binary Tree (preorder):")
tree.print_tree(tree.root)