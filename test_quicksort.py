import unittest
from quicksort import quicksort

class QuicksortTestCase(unittest.TestCase):
    """Test for 'quicksort.py.'"""

    def setUp(self):
        """Create a list to be sorted."""
        self.array = [6, 7, 2, 3, 8]

    def test_sort(self):
        """Is the array sortes."""
        array = quicksort(self.array)
        self.assertEqual(array, [2, 3, 6, 7, 8])

unittest.main()
