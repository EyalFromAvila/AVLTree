
from AVLTree import *

eyaltree = AVLTree()
eyaltree.insert(5, 5)
eyaltree.insert(10, 10)
eyaltree.insert(20,20)
eyaltree.insert(11, 11)
eyaltree.insert(4, 4)

# Print AVL tree
def print_avl_tree(node, prefix="", is_left=True):
    if node is None or not node.is_real_node():
        return
    # Print the right subtree
    print_avl_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    # Print the current node
    print(prefix + ("└── " if is_left else "┌── ") + f"({node.key}, {node.value})")
    # Print the left subtree
    print_avl_tree(node.left, prefix + ("    " if is_left else "│   "), True)
# Call the print function
print_avl_tree(eyaltree.root)