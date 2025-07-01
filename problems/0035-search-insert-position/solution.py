# Solution for Search Insert Position
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while right - left > 1:
            middle = (right + left) // 2
            if target <= nums[middle]:
                right = middle
            else:
                left = middle
        return right
