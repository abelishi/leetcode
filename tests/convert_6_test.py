import unittest
from problems.convert_6 import Solution

class Convert6Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_case_1(self):
        s = 'PAYPALISHIRING'
        numRows = 3
        self.assertEqual(self.solution.convert(s, numRows), 'PAHNAPLSIIGYIR')
    
    def test_case_2(self):
        s = 'PAYPALISHIRING'
        numRows = 4
        self.assertEqual(self.solution.convert(s, numRows), 'PINALSIGYAHRPI')
    
    def test_case_3(self):
        s = 'A'
        numRows = 1
        self.assertEqual(self.solution.convert(s, numRows), 'A')
