# Solution for Subarray Sum Equals K
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        accumulating_sum = 0
        hash_table = {0: 1}
        count = 0
        for i in range(len(nums)):
            accumulating_sum += nums[i]
            target = accumulating_sum - k
            count += hash_table.get(target, 0)
            hash_table[accumulating_sum] = hash_table.get(accumulating_sum, 0) + 1
        return count
