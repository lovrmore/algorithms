import unittest
from binary_search import binary

class BinaryTestCase(unittest.TestCase):
    """Tests for 'binary_search.py.'"""

    def setUp(self):
        """Create a list to be found"""
        self.list = [1, 3, 5, 7, 9]

    def test_found(self):
        """Is the mid 1"""
        item = binary(self.list, 3)
        self.assertEqual(item, 1)

    def test_not_found(self):
        """Is it return None"""
        item = binary(self.list, -1)
        self.assertEqual(item, None)

unittest.main()
