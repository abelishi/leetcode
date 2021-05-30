import unittest
from problems.two_sum import Solution

class TwoSumTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_case1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])
    
    def test_case2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])
    
    def test_case3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])
