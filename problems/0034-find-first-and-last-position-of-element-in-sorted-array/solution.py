# Solution for Find First And Last Position Of Element In Sorted Array
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_boundary, right_boundary = -1, -1
        if not nums:
            return [left_boundary, right_boundary]

        left, right = -1, len(nums)
        while right - left > 1:
            middle = (right + left) // 2
            if target <= nums[middle]:
                right = middle
            else:
                left = middle
        if 0 <= right < len(nums) and nums[right] == target:
            left_boundary = right

        left, right = left_boundary - 1, len(nums)
        while right - left > 1:
            middle = (right + left) // 2
            if target < nums[middle]:
                right = middle
            else:
                left = middle
        if 0 <= right - 1 < len(nums) and nums[right - 1] == target:
            right_boundary = right - 1

        return [left_boundary, right_boundary]
