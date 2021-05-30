from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2index = {}
        for i, num in enumerate(nums):
            num2index[num] = i
        
        for i, num in enumerate(nums):
            second = target - num
            if second in num2index.keys() and num2index[second] != i:
                return [i, num2index[second]]
