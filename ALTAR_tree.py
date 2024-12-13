#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  

## This file contains functions for the representation of binary trees.
## used in class Binary_search_tree's __repr__
## Written by a former student in the course - thanks to Amitai Cohen

def printree(t, bykey = True):
        """Print a textual representation of t
        bykey=True: show keys instead of values"""
        #for row in trepr(t, bykey):
        #        print(row)
        return trepr(t, bykey)

def trepr(t, bykey = False):
        """Return a list of textual representations of the levels in t
        bykey=True: show keys instead of values"""
        if t==None:
                return ["#"]

        thistr = str(t.key) if bykey else str(t.val)

        return conc(trepr(t.left,bykey), thistr, trepr(t.right,bykey))

def conc(left,root,right):
        """Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""
        
        lwid = len(left[-1])
        rwid = len(right[-1])
        rootwid = len(root)
        
        result = [(lwid+1)*" " + root + (rwid+1)*" "]
        
        ls = leftspace(left[0])
        rs = rightspace(right[0])
        result.append(ls*" " + (lwid-ls)*"_" + "/" + rootwid*" " + "\\" + rs*"_" + (rwid-rs)*" ")
        
        for i in range(max(len(left),len(right))):
                row = ""
                if i<len(left):
                        row += left[i]
                else:
                        row += lwid*" "

                row += (rootwid+2)*" "
                
                if i<len(right):
                        row += right[i]
                else:
                        row += rwid*" "
                        
                result.append(row)
                
        return result

def leftspace(row):
        """helper for conc"""
        #row is the first row of a left node
        #returns the index of where the second whitespace starts
        i = len(row)-1
        while row[i]==" ":
                i-=1
        return i+1

def rightspace(row):
        """helper for conc"""
        #row is the first row of a right node
        #returns the index of where the first whitespace ends
        i = 0
        while row[i]==" ":
                i+=1
        return i







"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int or None
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.val = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = 0
		self.bf = 0
		self.size = 1

	def __repr__(self):
		return "(" + str(self.key) + ":" + str(self.val) + ")"
		

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return not self.key == None
	

"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.sentinel = AVLNode(None,None)
		self.sentinel.size = 0
		self.sentinel.height = -1

	def __repr__(self): # no need to understand the implementation of this one
		out = ""
		for row in printree(self.root): # need printree.py file
			out = out + row + "\n"
		return out



	"""searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key
	"""
	def search(self, key: int):
		node = self.root
		if not node.is_real_node():
			return
		
		while node.is_real_node() and key != node.key:
			if key > node.key:
				node = node.right
			else:
				node = node.left
		
		return node


	"""inserts a new node into the dictionary with corresponding key and value
	
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def rotation(self, node):

		def right_rotation(Leftnode):
			# Rotation
			temp = Leftnode.right
			Leftnode.right = Leftnode.parent
			Leftnode.parent = Leftnode.right.parent 
			Leftnode.right.left = temp
			temp.parent = Leftnode.right
			Leftnode.right.parent = Leftnode
			
			# Fixing rank fields.
			if Leftnode.parent == self.sentinel:
				self.root = Leftnode
			else:
				if Leftnode.parent.key > Leftnode.key:
					Leftnode.parent.left = Leftnode
				else:
					Leftnode.parent.right = Leftnode
			Leftnode.right.height = max(Leftnode.right.left.height, Leftnode.right.right.height) + 1
			Leftnode.right.bf = Leftnode.right.left.height - Leftnode.right.right.height
			Leftnode.right.size = Leftnode.right.left.size + Leftnode.right.right.size + 1
			Leftnode.height = max(Leftnode.left.height,Leftnode.right.height) + 1
			Leftnode.bf = Leftnode.left.height- Leftnode.right.height
			Leftnode.size = Leftnode.right.size + Leftnode.left.size + 1

		# Rotation
		def left_rotation(Rightnode):
			# Rotation
			temp = Rightnode.left
			Rightnode.left = Rightnode.parent
			Rightnode.parent = Rightnode.left.parent
			Rightnode.left.right = temp
			temp.parent = Rightnode.left
			Rightnode.left.parent = Rightnode

			# Fixing rank fields.
			if Rightnode.parent == self.sentinel:
				self.root = Rightnode
			else:
				if Rightnode.parent.key > Rightnode.key:
					Rightnode.parent.left = Rightnode
				else:
					Rightnode.parent.right = Rightnode
			Rightnode.left.height = max(Rightnode.left.right.height, Rightnode.left.left.height) + 1
			Rightnode.left.bf = Rightnode.left.left.height - Rightnode.left.right.height
			Rightnode.left.size = Rightnode.left.left.size + Rightnode.left.right.size + 1
			Rightnode.height = max(Rightnode.left.height, Rightnode.right.height) + 1
			Rightnode.bf = Rightnode.left.height - Rightnode.right.height
			Rightnode.size = Rightnode.left.size + Rightnode.right.size + 1

		if node.bf == 2: # look at left child
			if node.left.bf == 1 or node.left.bf == 0:
				right_rotation(node.left)
			else:
				left_rotation(node.left.right)
				right_rotation(node.left)
		else:
			if node.right.bf == -1 or node.right.bf == 0:
				left_rotation(node.right)
			else:
				right_rotation(node.right.left)
				left_rotation(node.right)


	def insert(self, key, val):
		curr = self.root
		
		if curr is None:
			curr = AVLNode(key, val)
			self.root = curr
			curr.parent = curr.left = curr.right = self.sentinel
			return

		while True:
			curr.size += 1
			if curr.key < key:
				if not curr.right.is_real_node():
					curr.right = AVLNode(key, val)
					curr.right.left = curr.right.right = self.sentinel
					curr.right.parent = curr
					curr.height = max(curr.left.height, curr.right.height) + 1
					curr.bf = curr.left.height - curr.right.height
					curr = curr.right
					break
				else:
					curr = curr.right
			else:
				if not curr.left.is_real_node():
					curr.left = AVLNode(key, val)
					curr.left.left = curr.left.right = self.sentinel
					curr.left.parent = curr
					curr.height = max(curr.left.height, curr.right.height) + 1
					curr.bf = curr.left.height - curr.right.height
					curr = curr.left
					break
				else:
					curr = curr.left

		while curr.parent.is_real_node():
			curr = curr.parent
			curr.height = max(curr.right.height, curr.left.height) + 1
			curr.bf = curr.left.height - curr.right.height
			if abs(curr.bf) > 1:
				self.rotation(curr)
				break
		
	
	def Minimum(self, node):
		while node.left.is_real_node():
			node = node.left
		return node
	
	def Maximum(self, node):
		while node.right.is_real_node():
			node = node.right
		return node


	def Successor(self, node):
		if node.right.is_real_node():
			return self.Minimum(node.right)
		parent = node.parent
		temp = node.key
		while parent.is_real_node() and parent.key < temp:
			parent = parent.parent
		return parent
	
	def Predecessor(self, node):
		if node.left.is_real_node():
			return self.Maximum(node.left)
		parent = node.parent
		temp = node.key
		while parent.is_real_node() and parent.key > temp:
			parent = parent.parent
		return parent
		

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node: AVLNode):
		# Delete a node like a regular BST.
		node = self.search(node.key)
		parent = node.parent
		match node:
			case node if (not node.right.is_real_node()) and (not node.left.is_real_node()): # A leaf.
				if parent.is_real_node() and parent.key > node.key:
					parent.left = self.sentinel
				elif parent.is_real_node():
					parent.right = self.sentinel
				else:
					self.root = None
			case node if (not node.right.is_real_node()) or (not node.left.is_real_node()):
				if node.right is self.sentinel:
					child = node.left
				else:
					child = node.right
				if parent.is_real_node() and parent.key > node.key:
					parent.left = child
					child.parent = parent
				elif parent.is_real_node():
					parent.right = child
					child.parent = parent
				else:
					self.root = child
					child.parent = self.sentinel
			case _:
				successor = self.Successor(node)
				parent = successor.parent
				if self.root == node:
					self.root = successor

				if successor.parent == node:
					successor.left = parent.left
					successor.left.parent = successor
					successor.parent = parent.parent
					parent = successor
				else:
					if parent.left == successor:
						parent.left = successor.right
					else:
						parent.right = successor.right

					if successor.right.is_real_node():
						successor.right.parent = parent
					successor.right = node.right
					successor.right.parent = successor

					if successor.left.is_real_node():
						successor.left.parent = parent
					successor.left = node.left
					successor.left.parent = successor
					successor.parent = node.parent
				if node.parent.is_real_node():
					if node.parent.left == node:
						node.parent.left = successor
					else:
						node.parent.right = successor

		node.left = node.right = node.parent = None
		while parent.is_real_node():
			parent.bf = parent.left.height - parent.right.height
			parent.size -= 1
			new_height = max(parent.left.height, parent.right.height) + 1

			if (abs(parent.bf) < 2 and parent.height == new_height): # Balance is preserved up to root.
				return
			elif (abs(parent.bf) < 2 and parent.height != new_height): 
				parent.height = new_height
			else: # bf is 2. A rotation needed.
				self.rotation(parent)

			parent = parent.parent # Go on up until root.
			


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		curr = self.root
		stack = list()
		ans = list()

		while curr.is_real_node() or len(stack) != 0:
			while curr.is_real_node():
				stack.append(curr)
				curr = curr.left
			curr = stack.pop()
			ans.append(curr)
			curr = curr.right
		
		return ans


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.root.size

	"""compute the rank of node in the dictionary

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary to compute the rank for
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		node = node
		parent = node.parent
		rank = node.left.size + 1

		while parent.is_real_node():
			if parent.key < node.key: # We have turned left
				rank += parent.left.size + 1
			node = parent
			parent = parent.parent
		
		return rank


	"""finds the i'th smallest item (according to keys) in the dictionary

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: AVLNode
	@returns: the node of rank i in self
	"""
	def select(self, i):
		curr = self.root
		while True:
			if curr.left.size == i - 1:
				return curr
			if curr.left.size < i - 1:
				i -= (curr.left.size + 1)
				curr = curr.right
			else:
				curr = curr.left


	"""finds the node with the largest value in a specified range of keys

	@type a: int
	@param a: the lower end of the range
	@type b: int
	@param b: the upper end of the range
	@pre: a<b
	@rtype: AVLNode
	@returns: the node with maximal (lexicographically) value having a<=key<=b, or None if no such keys exist
	"""
	def max_range(self, a, b):
		arr = self.avl_to_array() #anyway its complexily is going to ba o(n)
		max = arr[a].value
		for i in range(a,b):
			if arr[i].value > max:
				max = arr[i].value
		return max
	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root



########################### Second Part

	def max_insert(self, key, val):
		curr = self.root
		
		if curr is None:
			curr = AVLNode(key, val)
			self.root = curr
			curr.parent = curr.left = curr.right = self.sentinel
			return

		while True:
			curr.size += 1
			if curr.key < key:
				if not curr.right.is_real_node():
					curr.right = AVLNode(key, val)
					curr.right.left = curr.right.right = self.sentinel
					curr.right.parent = curr
					curr.height = max(curr.left.height, curr.right.height) + 1
					curr.bf = curr.left.height - curr.right.height
					curr = curr.right
					break
				else:
					curr = curr.right
			else:
				if not curr.left.is_real_node():
					curr.left = AVLNode(key, val)
					curr.left.left = curr.left.right = self.sentinel
					curr.left.parent = curr
					curr.height = max(curr.left.height, curr.right.height) + 1
					curr.bf = curr.left.height - curr.right.height
					curr = curr.left
					break
				else:
					curr = curr.left

		while curr.parent.is_real_node():
			curr = curr.parent
			curr.height = max(curr.right.height, curr.left.height) + 1
			curr.bf = curr.left.height - curr.right.height
			if abs(curr.bf) > 1:
				self.rotation(curr)
				break
		