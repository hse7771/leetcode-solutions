# Solution for Jump Game
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        steps = nums[i]
        while i < n - 1 and steps != 0:
            i += 1
            steps -= 1
            steps = max(steps, nums[i])
        return i == n - 1
