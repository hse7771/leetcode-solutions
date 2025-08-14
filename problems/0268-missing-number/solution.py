# Solution for Missing Number
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (1 + n) * n // 2
        return s - sum(nums)
