import unittest
from common.binary_search import BinarySearch

class BinarySearchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.binary_search = BinarySearch()

    def test_case1(self) -> None:
        sorted_list = [1, 2, 3, 4, 5, 5, 6]
        target = 5
        self.assertEqual(self.binary_search.upper_bound(sorted_list, target), 6)
        self.assertEqual(self.binary_search.lower_bound(sorted_list, target), 4)

    def test_case2(self) -> None:
        sorted_list = [1, 2, 3, 4, 5, 5, 6]
        target = 0
        self.assertEqual(self.binary_search.upper_bound(sorted_list, target), 0)
        self.assertEqual(self.binary_search.lower_bound(sorted_list, target), 0)
    
    def test_case3(self) -> None:
        sorted_list = [1, 2, 3, 4, 5, 5, 6]
        target = 10
        self.assertEqual(self.binary_search.upper_bound(sorted_list, target), 7)
        self.assertEqual(self.binary_search.lower_bound(sorted_list, target), 7)
    
    def test_case4(self) -> None:
        sorted_list = [1, 2, 3, 4, 5, 5, 6]
        target = 2
        self.assertEqual(self.binary_search.upper_bound(sorted_list, target), 2)
        self.assertEqual(self.binary_search.lower_bound(sorted_list, target), 1)