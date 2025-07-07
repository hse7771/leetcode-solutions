# Solution for Two Sum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        answer = []
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hash_table:
                answer = [i, hash_table[key]]
                break
            if nums[i] not in hash_table:
                hash_table[nums[i]] = i
        return answer
