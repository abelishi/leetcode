class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        # ignore space at the begining
        s = s.strip()
        sign = 1
        if s.startswith('-'):
            sign = -1
            s = s[1:]
        elif s.startswith('+'):
            sign = 1
            s = s[1:]

        i = 0
        ans = 0
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            ans = ans * 10 + (ord(s[i]) - ord('0'))
            i += 1

        ans = sign * ans
        if ans < INT_MIN:
            return INT_MIN
        elif ans > INT_MAX:
            return INT_MAX
        else:
            return ans
