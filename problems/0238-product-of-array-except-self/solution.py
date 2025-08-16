# Solution for Product Of Array Except Self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left = nums[0]
        for i in range(1, n):
            result[i] = left
            left *= nums[i]
        right = nums[n - 1]
        for j in range(n - 2, -1, -1):
            result[j] *= right
            right *= nums[j]

        return result
