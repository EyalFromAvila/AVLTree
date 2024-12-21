from AVLTree import AVLTree
from AVLTree import AVLNode

# Initialize AVL tree
Yashatree = AVLTree()

# Insert nodes
Yashatree.insert(5, 'v5')
#Yashatree.insert_as_child(Yashatree.root, AVLNode(7, 'v7'), 0)
#Yashatree.insert_as_child(Yashatree.root, AVLNode(6, 'v6'), 0)
Yashatree.insert(6, 'v6')
Yashatree.insert(7, 'v7')

Yashatree.insert(4, 'v4')
Yashatree.insert(2, 'v2')



# Debug: Check root and its children
print("Tree Root:", Yashatree.root.key if Yashatree.root else "None")
print("Root Left:", Yashatree.root.left.key if Yashatree.root and Yashatree.root.left else "None")
print("Root Right:", Yashatree.root.right.key if Yashatree.root and Yashatree.root.right else "None")

# Print AVL tree
def print_avl_tree(node, prefix="", is_left=True):
    if node is None or not node.is_real_node():
        return

    print_avl_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + f"({node.key}, {node.value})")
    print_avl_tree(node.left, prefix + ("    " if is_left else "│   "), True)


def print_avl_tree_asaf(node, space=0, level_spacing=5):
    # בסיס הרקורסיה
    if node is None or not node.is_real_node:
        return

    space += level_spacing
    print_avl_tree_asaf(node.right, space, level_spacing)
    print()
    print(" " * (space - level_spacing) + f"[{node.key}]")
    print_avl_tree_asaf(node.left, space, level_spacing)


# Call the print function

print_avl_tree_asaf(Yashatree.root)
print_avl_tree(Yashatree.root)