from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_index = 0
        right_index = len(height) - 1
        while left_index < right_index:
            max_area_temp = (right_index - left_index) * min(height[left_index], height[right_index])
            max_area = max(max_area, max_area_temp)
            if height[left_index] > height[right_index]:
                right_index -= 1
            else:
                left_index += 1
        
        return max_area
