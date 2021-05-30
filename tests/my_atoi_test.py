import unittest

from problems.my_atoi import Solution

class MyAtoiTest(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_case_1(self):
        s = '42'
        self.assertEqual(self.solution.myAtoi(s), 42)
    
    def test_case_2(self):
        s = '   -42'
        self.assertEqual(self.solution.myAtoi(s), -42)
    
    def test_case_3(self):
        s = '4193 with words'
        self.assertEqual(self.solution.myAtoi(s), 4193)
    
    def test_case_4(self):
        s = 'words and 987'
        self.assertEqual(self.solution.myAtoi(s), 0)

    def test_case_5(self):
        s = '-91283472332'
        self.assertEqual(self.solution.myAtoi(s), -2147483648)
