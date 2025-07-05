# Solution for Majority Element

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == key:
                count += 1
            elif count == 0:
                key = nums[i]
                count += 1
            else:
                count -= 1
        return key


# Naive solution:
# Use frequency hash table
