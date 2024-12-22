from AVLTree import AVLTree
from AVLTree import AVLNode

# Initialize AVL tree
Yashatree = AVLTree()

# Insert nodes
Yashatree.insert(5, 'v5')
Yashatree.insert(6, 'v6')
Yashatree.insert(7, 'v7')

#Yashatree.insert(4, 'v4')
Yashatree.insert(1, 'v1')
Yashatree.insert(0, 'v0')

#Yashatree.insert(8, 'v8')
#Yashatree.recompute_heights(Yashatree.search(8))


Yashatree.insert(11, 'v11')
Yashatree.insert(12, 'v12')
Yashatree.insert(3, 'v3')



# Print AVL tree
def print_avl_tree(node, prefix="", is_left=True):
    if node is None or not node.is_real_node():
        return

    print_avl_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + f"({node.key}, {node.value})")
    print_avl_tree(node.left, prefix + ("    " if is_left else "│   "), True)

print(Yashatree.search(11))
print(Yashatree.finger_search(11))



# Call the print function
print_avl_tree(Yashatree.root)


