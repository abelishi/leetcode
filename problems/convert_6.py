class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        s_new = ''
        n = len(s)
        cycle_len = 2 * numRows - 2
        for i in range(numRows):
            for j in range(0, n - i, cycle_len):
                s_new += s[i + j]
                if i != 0 and i != numRows-1 and j + cycle_len -i < n:
                    s_new += s[j + cycle_len - i]
        return s_new