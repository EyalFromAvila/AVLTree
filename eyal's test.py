
from AVLTree import *

eyaltree = AVLTree()
eyaltree.insert(10, 10)
eyaltree.insert(20, 20)
eyaltree.insert(30, 30)
eyaltree.insert(40, 40)
eyaltree.insert(50, 50)
eyaltree.insert(60, 60)
eyaltree.insert(70, 70)
eyaltree.insert(80, 80)
eyaltree.insert(90, 90)
eyaltree.insert(100, 100)
eyaltree.insert(110, 110)

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

tree2 = AVLTree()
tree2.insert(1, 1)
tree2.insert(2, 2)
tree2.insert(3, 3)

eyaltree.join(tree2, 4,4)

print_avl_tree(eyaltree.root)
