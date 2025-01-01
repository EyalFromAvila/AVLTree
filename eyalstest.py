
from AVLTree import *

eyaltree = AVLTree()
eyaltree.insert(1,1)


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
