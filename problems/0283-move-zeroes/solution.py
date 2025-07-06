# Solution for Move Zeroes
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cur_insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur_insert] = nums[i]
                cur_insert += 1
        for j in range(cur_insert, len(nums)):
            nums[j] = 0
