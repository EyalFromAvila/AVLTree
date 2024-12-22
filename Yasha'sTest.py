from AVLTree import AVLTree
from AVLTree import AVLNode

# Print AVL tree
def print_avl_tree(node, prefix="", is_left=True):
    if node is None or not node.is_real_node():
        return

    print_avl_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + f"({node.key}, {node.value})")
    print_avl_tree(node.left, prefix + ("    " if is_left else "│   "), True)


# Initialize AVL tree
Yashatree = AVLTree()





# Insert nodes
Yashatree.insert(5, 'v5')
Yashatree.insert(6, 'v6')
Yashatree.insert(7, 'v7')
Yashatree.insert(1, 'v1')
Yashatree.insert(0, 'v0')
Yashatree.insert(11, 'v11')
Yashatree.insert(12, 'v12')
Yashatree.insert(3, 'v3')
Yashatree.insert(110, 'v110')
Yashatree.insert(1100, 'v1100')
Yashatree.insert(130, 'v130')
Yashatree.insert(1300, 'v1300')




print(Yashatree.search(11))
print(Yashatree.pointer_only(11))
print(int(Yashatree.pointer_only(5).balance()))


# Call the print function
print_avl_tree(Yashatree.root)

print(int(Yashatree.pointer_only(1300).balance()))



