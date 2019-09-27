import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        #Tests for the max being at the end of the list
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        #Tests for the max being in the middle of the list
        self.assertEqual(max_list_iter([1, 3, 2]), 3)
        #Tests for the max being at the start of the list
        self.assertEqual(max_list_iter([3, 2, 1]), 3)
        #Tests for the max being all the numbers in the list
        self.assertEqual(max_list_iter([3, 3, 3]), 3)
        #Tests for the max being some of the numbers in the list
        self.assertEqual(max_list_iter([1, 3, 3]), 3)
        # Tests for lists of greater size and random composition
        self.assertEqual(max_list_iter([1, 2, 8, 4, 5, 5, 9, 6]), 9)


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])                         # Tests for a list of size 3
        self.assertEqual(reverse_rec([1,2,3,4,5,6,7]), [7,6,5,4,3,2,1])        # Tests for a list of size 7
        self.assertEqual(reverse_rec([1,2]), [2,1])                            # Tests for a list of size 2
        self.assertEqual(reverse_rec([1]), [1])                                # Tests for a list of size 1
        self.assertEqual(reverse_rec([]),[])                                   # Tests for an empty list


    def test_bin_search(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        list_val =[0,1,2,3,4,7,8,9,10]                                            # Sets the list
        low = 0                                                                   # Sets the low equal to 0
        high = len(list_val)-1                                                    # Sets the high equal to the number of elements in the list
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )         # Tests for a value in the middle of the list
        list_val = [0, 1, 2, 3]
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 1)        # Tests for a value in the second position in the list
        list_val = [10, 12, 13, 15, 25, 34, 40, 42, 44, 56, 60]
        self.assertEqual(bin_search(44, 0, len(list_val) - 1, list_val), 8)       # Tests for a value near the end of the list
        list_val = [10, 12, 13, 15, 25, 34, 40, 42, 44, 56, 60]
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 0)       # Tests for a value at the start of the list
        list_val = [10, 12, 13, 15, 25, 34, 40, 42, 44, 56, 60]
        self.assertEqual(bin_search(25, 0, len(list_val) - 1, list_val), 4)       # Tests for a value near the middle of the list
        list_val = [10, 12, 13, 15, 25, 34, 40, 42, 44, 56, 60]
        self.assertEqual(bin_search(60, 0, len(list_val) - 1, list_val), 10)      # Tests for a value at the end of the list
        list_val = [10, 12, 13, 15, 25, 34, 40, 42, 44, 56, 60]
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), None)     # Tests for a value not in the list


if __name__ == "__main__":
        unittest.main()

