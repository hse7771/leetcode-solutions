# Solution for Continuous Subarray Sum
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = nums[0] % k
        hash_table = {s: 0}
        for i in range(1, len(nums)):
            s = (s + nums[i] % k) % k
            r = (s - k) % k
            if r in hash_table and i - hash_table[r] > 1:
                return True
            elif s == 0:
                return True
            if s not in hash_table:
                hash_table[s] = i
        return False
