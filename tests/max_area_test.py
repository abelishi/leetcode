import unittest
from problems.max_area import Solution

class MaxAreaTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_case1(self):
        height = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(self.solution.maxArea(height), 49)
    
    def test_case2(self):
        height = [1,1]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_case3(self):
        height =  [4,3,2,1,4]
        self.assertEqual(self.solution.maxArea(height), 16)
    
    def test_case4(self):
        height = [1, 2, 1]
        self.assertEqual(self.solution.maxArea(height), 2)
