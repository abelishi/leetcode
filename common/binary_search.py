import typing
from typing import List

class BinarySearch(object):

    @staticmethod
    def upper_bound(sorted_list: List, target) -> int:
        left = 0
        right = len(sorted_list) - 1
        while left < right:
            middle = left + (right - left) // 2
            if sorted_list[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        
        if right == len(sorted_list) - 1 and target >= sorted_list[-1]:
            return len(sorted_list)

        return right

    @staticmethod
    def lower_bound(sorted_list: List, target) -> int:
        left = 0
        right = len(sorted_list) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if sorted_list[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        
        return left