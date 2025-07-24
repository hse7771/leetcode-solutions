# Solution for Longest Subarray Of 1'S After Deleting One Element
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 0
        prev = cur = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                prev = cur
                cur = 0
            mx = max(mx, prev + cur)
        if mx == len(nums):
            mx -= 1
        return mx
