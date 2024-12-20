# id1: 206405417
# name1: Eyal Sapir
# username1: eyalsapir
# id2: 209860188
# name2: Iakov Odesser
# username2: iakovodesser

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1



    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.height != -1

    def height_difference(self):
        return self.left.height - self.right.height

    def max_children_height(self):
        return max(self.left.height, self.right.height)


"""
A class implementing an AVL tree.
"""


def get_successor(node):
    current = node
    while current.left.is_real_node():
        current = current.left
    return current


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self):
        self.root = None
        self.max = None
        self.size = 0
        self.external = None

    """searches for a node in the dictionary corresponding to the key (starting at the root)

    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def search(self, key):
        return self.search_from_node(self.root, key, 1)

    """
    Helper function that kinda does all the work recursively 
    """
    def search_from_node(self, node, key, depth):
        # base cases
        if key is None:
            return None, depth
        if node.key == key:
            return node, depth

        # process
        if node.key < key:
            return self.search_from_node(node.left, key, depth + 1)
        if node.key > key:
            return self.search_from_node(node.right, key, depth + 1)

    """searches for a node in the dictionary corresponding to the key, starting at the max

    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def finger_search(self, key):
        current = self.max
        edges_passed = 0

        # Climb up the tree until a node's subtree is larger than k
        while current.parent and current.size < key:
            current = current.parent
            edges_passed += 1

        # Perform the regular search starting from this node
        result_key, result_edges = self.search_from_node(current, key, edges_passed)

        return result_key, 1 + result_edges

    """inserts a new node into the dictionary with corresponding key and value (starting at the root)

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int)
    @returns: a 3-tuple (x,e,h) where x is the new node,
    e is the number of edges on the path between the starting node and new node before rebalancing,
    and h is the number of PROMOTE cases during the AVL rebalancing
    """

    """
    Helper function that kinda does all the work
    """
    def insert_as_child(self, parent_node, child_node, path): #DOESN'T INCREMENT SIZE!!!
        node_to_rebalance = None
        promotions = 0

        # key is smaller than root
        if child_node.key < parent_node.key:
            if not parent_node.left:
                parent_node.left = child_node
                child_node.parent = parent_node
                # do promotions
                if parent_node.height == 0:
                    current = parent_node
                    while current:
                        current.height = current.max_children_height() + 1
                        promotions += 1
                        path += 1
                        if not current.height_difference() in [-1, 0, 1]:
                            node_to_rebalance = current
                            break
                        current = current.parent
            else:
                self.insert_as_child(parent_node.left, child_node, path + 1)

            # key is bigger than root
            if child_node.key > parent_node.key:
                if not parent_node.right:
                    parent_node.right = child_node
                    child_node.parent = parent_node
                    if parent_node.height == 0:
                        current = parent_node
                        while current:
                            current.height = current.max_children_height() + 1
                            current.size += 1
                            promotions += 1
                            path += 1
                            if not current.height_difference() in [-1, 0, 1]:
                                node_to_rebalance = current
                                break
                            current = current.parent
                else:
                    self.insert_as_child(parent_node.right, child_node, path + 1)

            if node_to_rebalance:
                self.rebalance(node_to_rebalance)
            if child_node.key > self.max:
                self.max = child_node.key
        return child_node, path, promotions

    def insert(self, key, val):
        inserted_node = AVLNode(key, val)
        inserted_node.left = self.external
        inserted_node.right = self.external
        if not self.root:
            self.root = inserted_node
            self.max = inserted_node
            self.size = 1
            return inserted_node, 0, 0
        else:
            self.size += 1
            return self.insert_as_child(self.root, inserted_node, 0)

    """
    Helper function to keep track of heights 
    """
    def recompute_heights(self, start_from_node):
        changed = True
        node = start_from_node
        while node and changed:
            old_height = node.height
            node.height = node.max_children_height() + 1
            changed = node.height != old_height
            node = node.parent

    """
    Helper function to restore balance 
    """
    def rebalance(self, node_to_rebalance):
        A = node_to_rebalance  # The unbalanced node
        F = A.parent  # The parent of the unbalanced node

        # Right-Heavy Case
        if node_to_rebalance.balance() == -2:

            # Right-Right (RR) Imbalance
            if node_to_rebalance.right.balance() <= 0:
                B = A.right
                C = B.right

                assert (A.is_real_node() and B.is_real_node() and C.is_real_node())  # maybe delete this line later

                # Left Rotation
                A.right = B.left
                if A.right.is_real_node():
                    A.right.parent = A
                B.left = A
                A.parent = B

                # Fixing parentage and heights
                if F is None:
                    self.root = B
                    self.root.parent = None
                else:
                    if F.right == A:
                        F.right = B
                    else:
                        F.left = B
                    B.parent = F
                self.recompute_heights(A)
                self.recompute_heights(B.parent)

            # Right-Left (RL) Imbalance
            else:
                B = A.right
                C = B.left

                assert (A.is_real_node() and B.is_real_node() and C.is_real_node())  # maybe delete this line later

                # Right rotation on B, then left rotation on A
                B.left = C.right
                if B.left:
                    B.left.parent = B
                A.right = C.left
                if A.right:
                    A.right.parent = A
                C.right = B
                B.parent = C
                C.left = A
                A.parent = C

                # Fixing parentage and heights
                if F is None:
                    self.root = C
                    self.root.parent = None
                else:
                    if F.right == A:
                        F.right = C
                    else:
                        F.left = C
                    C.parent = F
                self.recompute_heights(A)
                self.recompute_heights(B)

        # Left-Heavy Case
        else:
            assert (node_to_rebalance.balance() == +2)

            # Left-Left (LL) Imbalance
            if node_to_rebalance.left.balance() >= 0:
                B = A.left
                C = B.left

                assert (A.is_real_node() and B.is_real_node() and C.is_real_node())  # maybe delete this line later

                # Single right rotation
                A.left = B.right
                if (A.left):
                    A.left.parent = A
                B.right = A
                A.parent = B

                # Fixing parentage and heights
                if F is None:
                    self.root = B
                    self.root.parent = None
                else:
                    if F.right == A:
                        F.right = B
                    else:
                        F.left = B
                    B.parent = F
                self.recompute_heights(A)
                self.recompute_heights(B.parent)

            # Left-Right (LR) Imbalance
            else:
                B = A.left
                C = B.right

                assert (A.is_real_node() and B.is_real_node() and C.is_real_node())  # maybe delete this line later

                # Left rotation on B, then right rotation on A
                A.left = C.right
                if A.left:
                    A.left.parent = A
                B.right = C.left
                if B.right:
                    B.right.parent = B
                C.left = B
                B.parent = C
                C.right = A
                A.parent = C

                # Fixing parentage and heights
                if F is None:
                    self.root = C
                    self.root.parent = None
                else:
                    if (F.right == A):
                        F.right = C
                    else:
                        F.left = C
                    C.parent = F
                self.recompute_heights(A)
                self.recompute_heights(B)

    """inserts a new node into the dictionary with corresponding key and value, starting at the max

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int)
    @returns: a 3-tuple (x,e,h) where x is the new node,
    e is the number of edges on the path between the starting node and new node before rebalancing,
    and h is the number of PROMOTE cases during the AVL rebalancing
    """

    def finger_insert(self, key, val):
        new_node = AVLNode(key, val)
        current = self.max
        upward_path = 0

        # Climb up the tree until a node's subtree is larger than k
        while current.parent and current.size < key:
            current = current.parent
            upward_path += 1

        # Starting from there do the insert
        inserted_node, downward_path, promotions = self.insert_as_child(current, new_node, 0)
        self.size += 1
        return inserted_node, downward_path + upward_path, promotions

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    """

    def delete(self, node):
        parent = node.parent

        # Node is leaf
        if not node.left.is_real_node() and not node.right.is_real_node():
            if parent:
                if parent.left == node:
                    parent.left = None
                if parent.right == node:
                    parent.right = None

            else:
                self.root = None  # Node is root

        # Node has only left child
        elif node.left.is_real_node() and not node.right.is_real_node():
            self.switcheroo(node, node.left)

        # Node has only right child
        elif not node.left.is_real_node() and node.right.is_real_node():
            self.switcheroo(node, node.right)

        # Node has two children
        else:
            successor = get_successor(node)
            node.key, node.val = successor.key, successor.val
            self.delete(successor)

        # Rebalancing and heights fixing
        if parent:
            self.recompute_heights(parent)  # Update heights starting from the parent
            while parent:
                self.rebalance(parent)  # Rebalance each ancestor node
                parent = parent.parent

        self.size -= 1
    """
    Helper function to replace a node in the tree with a new node.
    """
    def switcheroo(self, old_node, new_node):
        parent = old_node.parent
        if parent:
            if parent.left == old_node:
                parent.left = new_node
            else:
                parent.right = new_node

        else:  # Replacing the root
            self.root = new_node
        if new_node:
            new_node.parent = parent

    """joins self with item and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: the key separting self and tree2
    @type val: string
    @param val: the value corresponding to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
    or the opposite way
    """

    """
    Helper functions to see which tree is more attractive
    """
    def key_size_matters(self, tree2):
        if self.root.key > tree2.root.key:
            return self, tree2
        else:
            return tree2, self

    def height_matters(self, tree2):
        if self.root.height > tree2.root.height:
            return self, tree2
        else:
            return tree2, self

    def join(self, tree2, key, val):
        # naming
        big_keys_tree, small_keys_tree = self.key_size_matters(tree2)
        taller_tree, shorter_tree = self.height_matters(tree2)
        k = AVLNode(key, val)
        self.max = big_keys_tree.max
        self.size = self.size + tree2.size + 1

        # Easy case: same size
        if abs(big_keys_tree.root.height - small_keys_tree.root.height) <= 1:
            k.left, k.right = small_keys_tree.root, big_keys_tree.root
            self.root = k
            k.height = k.max_children_height() + 1

        # Tough case: One tree is significantly taller
        curr = taller_tree.root
        target_height = shorter_tree.root.height + 1

        # Traverse down the taller tree to find the correct attachment point
        if taller_tree == big_keys_tree:
            while curr.height > target_height:
                curr = curr.left

            # Attach shorter tree as left subtree of `k`
            k.left = shorter_tree.root
            if k.left.is_real_node():
                k.left.parent = k
            k.right = curr.left
            if k.right.is_real_node():
                k.right.parent = k
            curr.left = k
        else:
            while curr.height > target_height:
                curr = curr.right

            # Attach shorter tree as right subtree of `k`
            k.right = shorter_tree.root
            if k.right.is_real_node():
                k.right.parent = k
            k.left = curr.right
            if k.left.is_real_node():
                k.left.parent = k
            curr.right = k
        k.parent = curr
        # Recompute heights and rebalance

        self.recompute_heights(k)
        self.rebalance(curr)
        self.root = taller_tree.root


    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: the node in the dictionary to be used for the split
    @rtype: (AVLTree, AVLTree)
    @returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        return None, None

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        return None

    """returns the node with the maximal key in the dictionary

    @rtype: AVLNode
    @returns: the maximal node, None if the dictionary is empty
    """

    def max_node(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return -1

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return None
