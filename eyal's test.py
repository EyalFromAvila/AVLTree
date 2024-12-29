
from AVLTree import *

eyaltree = AVLTree()
eyaltree.insert(1, 1)
eyaltree.insert(2, 2)
eyaltree.insert(3, 3)
eyaltree.insert(4, 4)
eyaltree.insert(5, 5)
eyaltree.insert(6, 6)
eyaltree.insert(7, 7)
eyaltree.insert(8, 8)
eyaltree.insert(9, 9)
eyaltree.insert(10, 10)
eyaltree.insert(11, 11)
eyaltree.insert(12, 12)
eyaltree.insert(13, 13)
eyaltree.insert(14, 14)
eyaltree.insert(15, 15)

# Print AVL tree
def print_avl_tree(node, prefix="", is_left=True):
    underline = "\033[1m"
    reset = "\033[0m"
    if node is None or not node.is_real_node():
        return
    # Print the right subtree
    print_avl_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    # Print the current node
    print(prefix + ("└── " if is_left else "┌── ") + f"{underline}{node.key}{reset}")
    # Print the left subtree
    print_avl_tree(node.left, prefix + ("    " if is_left else "│   "), True)
# Call the print function
print_avl_tree(eyaltree.root)