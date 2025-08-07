# Solution for 3Sum Closest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = None
        diff_closest = 10**8
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(target - s)
                if diff < diff_closest:
                    diff_closest = diff
                    closest_sum = s
                if s > target:
                    r -= 1
                else:
                    l += 1
        return closest_sum
