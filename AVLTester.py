import unittest
from AVLTree import AVLTree


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        """Initialize an AVL Tree instance for testing."""
        self.tree = AVLTree()  # Assuming AVLTree is your class name.

    def test_insert(self):
        """Test the insert method."""
        # Insert into an empty tree
        self.tree.insert(10, "value10")
        self.assertEqual(self.tree.search(10), (10, "value10"))

        # Insert multiple keys
        self.tree.insert(20, "value20")
        self.tree.insert(5, "value5")
        self.assertEqual(self.tree.search(20), (20, "value20"))
        self.assertEqual(self.tree.search(5), (5, "value5"))

        # Test AVL property
        self.assertTrue(self.check_avl_property(self.tree.root))

    def test_delete(self):
        """Test the delete method."""
        self.tree.insert(10, "value10")
        self.tree.insert(20, "value20")
        self.tree.insert(5, "value5")

        # Delete a leaf node
        self.tree.delete(5)
        self.assertIsNone(self.tree.search(5))

        # Delete a node with one child
        self.tree.delete(20)
        self.assertIsNone(self.tree.search(20))

        # Delete the root
        self.tree.delete(10)
        self.assertIsNone(self.tree.search(10))

        # Test AVL property
        self.assertTrue(self.check_avl_property(self.tree.root))

    def test_search(self):
        """Test the search method."""
        self.tree.insert(10, "value10")
        self.tree.insert(20, "value20")
        self.tree.insert(5, "value5")

        # Search for existing keys
        self.assertEqual(self.tree.search(10), (10, "value10"))
        self.assertEqual(self.tree.search(20), (20, "value20"))
        self.assertEqual(self.tree.search(5), (5, "value5"))

        # Search for non-existent key
        self.assertIsNone(self.tree.search(15))

    def test_split(self):
        """Test the split method."""
        self.tree.insert(10, "value10")
        self.tree.insert(20, "value20")
        self.tree.insert(5, "value5")

        t1, t2 = self.tree.split(10)

        # Verify split properties
        self.assertTrue(self.check_avl_property(t1.root))
        self.assertTrue(self.check_avl_property(t2.root))

    def check_avl_property(self, node):
        """Check if the AVL property holds for the tree."""
        if node is None:
            return True

        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1

        # Check balance factor
        if abs(left_height - right_height) > 1:
            return False

        # Recursively check subtrees
        return self.check_avl_property(node.left) and self.check_avl_property(node.right)


if __name__ == "__main__":
    unittest.main()
