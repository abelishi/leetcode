import unittest
from problems.ismatch_10 import Solution

class IsMatchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_case1(self):
        s = 'aa'
        p = 'a'
        self.assertEqual(self.solution.isMatch(s, p), False)
    
    def test_case2(self):
        s = 'aa'
        p = 'a*'
        self.assertEqual(self.solution.isMatch(s, p), True)
    
    def test_case3(self):
        s = 'ab'
        p = '.*'
        self.assertEqual(self.solution.isMatch(s, p), True)
    
    def test_case4(self):
        s = 'aab'
        p = 'c*a*b'
        self.assertEqual(self.solution.isMatch(s, p), True)
    
    def test_case5(self):
        s = 'mississippi'
        p = 'mis*is*p*.'
        self.assertEqual(self.solution.isMatch(s, p), False)

    def test_case6(self):
        s = 'aaa'
        p = 'a*a'
        self.assertEqual(self.solution.isMatch(s, p), True)

    def test_case7(self):
        s = 'a'
        p = 'ab*a'
        self.assertEqual(self.solution.isMatch(s, p), False)

    def test_case8(self):
        s = 'bbab'
        p = 'b*a*'
        self.assertEqual(self.solution.isMatch(s, p), False)
