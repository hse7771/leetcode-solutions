# Solution for Subarray Product Less Than K
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        p_i = 0
        count = 0
        n = len(nums)
        for i in range(n):
            p *= nums[i]
            while p >= k and p_i <= i:
                p //= nums[p_i]
                p_i += 1
            count += (i - p_i + 1)
        return count
