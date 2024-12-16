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
        self.size = 0

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.height != -1

    def height_difference(self):
        return self.leftChild.height - self.rightChild.height

    def max_children_height(self):
        return max(self.leftChild.height, self.rightChild.height)

"""
A class implementing an AVL tree.
"""
class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self):
        self.root = None
        self.max = None
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

    def search_from_node(self, node, key, depth):
        # base cases
        if key is None:
            return None, depth
        if node.key == key:
            return node, depth

        # process
        if node.key < key:
            return self.search_from_node(node.left, key, depth + 1)
        if self.key > key:
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
        result_key, result_edges = current.search_from_node(self, edges_passed)
        result_edges += edges_passed

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

    def insert_as_child(self, parent_node, child_node, path):
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
                        current.size += 1
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
        inserted_node.size = 1
        if not self.root:
            self.root = inserted_node
            self.max = inserted_node
            return inserted_node, 0, 0
        else:
            return self.insert_as_child(self.root, inserted_node, 0)

    def recompute_heights(self, start_from_node): ###still need to recompute subtree sizes too!!!!
        changed = True
        node = start_from_node
        while node and changed:
            old_height = node.height
            node.height = node.max_children_height() + 1
            changed = node.height != old_height
            node = node.parent

    def rebalance(self, node_to_rebalance):
        A = node_to_rebalance
        F = A.parent
        if node_to_rebalance.balance() == -2:
            if node_to_rebalance.rightChild.balance() <= 0:
                B = A.rightChild
                C = B.rightChild
                assert (A.is_real_node() and B.is_real_node() and C.is_real_node()) #maybe delete this line later
                A.rightChild = B.leftChild
                if A.rightChild.is_real_node():
                    A.rightChild.parent = A
                B.leftChild = A
                A.parent = B
                if F is None:
                    self.root = B
                    self.root.parent = None
                else:
                    if F.rightChild == A:
                        F.rightChild = B
                    else:
                        F.leftChild = B
                    B.parent = F
                self.recompute_heights(A)
                self.recompute_heights(B.parent)
            else:
                B = A.rightChild
                C = B.leftChild
                assert (A.is_real_node() and B.is_real_node() and C.is_real_node()) #maybe delete this line later
                B.leftChild = C.rightChild
                if B.leftChild:
                    B.leftChild.parent = B
                A.rightChild = C.leftChild
                if A.rightChild:
                    A.rightChild.parent = A
                C.rightChild = B
                B.parent = C
                C.leftChild = A
                A.parent = C
                if F is None:
                    self.root = C
                    self.root.parent = None
                else:
                    if F.rightChild == A:
                        F.rightChild = C
                    else:
                        F.leftChild = C
                    C.parent = F
                self.recompute_heights(A)
                self.recompute_heights(B)
        else:
            assert (node_to_rebalance.balance() == +2)
            if node_to_rebalance.leftChild.balance() >= 0:
                B = A.leftChild
                C = B.leftChild
                assert (A.is_real_node() and B.is_real_node() and C.is_real_node()) #maybe delete this line later
                A.leftChild = B.rightChild
                if (A.leftChild):
                    A.leftChild.parent = A
                B.rightChild = A
                A.parent = B
                if F is None:
                    self.root = B
                    self.root.parent = None
                else:
                    if F.rightChild == A:
                        F.rightChild = B
                    else:
                        F.leftChild = B
                    B.parent = F
                self.recompute_heights(A)
                self.recompute_heights(B.parent)
            else:
                B = A.leftChild
                C = B.rightChild
                assert (A.is_real_node() and B.is_real_node() and C.is_real_node()) #maybe delete this line later
                A.leftChild = C.rightChild
                if A.leftChild:
                    A.leftChild.parent = A
                B.rightChild = C.leftChild
                if B.rightChild:
                    B.rightChild.parent = B
                C.leftChild = B
                B.parent = C
                C.rightChild = A
                A.parent = C
                if F is None:
                    self.root = C
                    self.root.parent = None
                else:
                    if (F.rightChild == A):
                        F.rightChild = C
                    else:
                        F.leftChild = C
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
        return None, -1, -1

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    """

    def delete(self, node):
        return

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

    def join(self, tree2, key, val):
        return

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


