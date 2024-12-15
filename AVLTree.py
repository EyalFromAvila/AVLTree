# id1: 206405417
# name1: Eyal Sapir
# username1: eyalsapir
# id2: 209860188
# name2: Iakov Odesser
# username2: iakovodesser

import math
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
        if self.height == -1:
            return False


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self):
        self.root = None

    def _height_difference(self, node):
        if node.is_real_node:
            return node.left.height - node.right.height


"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

"""time complexity O(logn) since tree is AVL hence balanced"""


def search(self, key):
    def search_helper(node, target_key, depth):
        if node is None:
            return None, -1
        if node.key == target_key:
            return node, depth
        if target_key < node.key:
            return search_helper(node.left, target_key, depth + 1)
        else:
            return search_helper(node.right, target_key, depth + 1)

        return search_helper(self.root, key, 0)

    """searches for a node in the dictionary corresponding to the key, starting at the max
        
    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def finger_search(self, key):

        # Start at the smallest node
        current = self.minimum

        if not current:
        return None, -1  # Tree is empty

    edges_passed = 0

    # Climb up the tree until a node's subtree is larger than k
    while current.parent and current.height < math.log2(key):
        current = current.parent
        edges_passed += 1

    # Perform the regular search starting from this node
    result_key, result_edges = self.search_from_node(current, key)
    if result_key is not None:
        # Add the edges passed during the initial climb
        return result_key, edges_passed + result_edges

    return None, -1  # Key not found


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

def search_for_insert(self, key):
    if not self.root.is_real_node:
        return self.root

    if self.root.key < key:
        return self.search_for_insert(self.root.right)
    else:
        return self.search_for_insert(self.root.left)
def insert(self, key, val):
    inserted = AVLNode(search_for_insert(self, key))

    return None, -1, -1

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


