# Solution for Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        a0, a1 = 1, 1
        for step in range(1, n):
            a0, a1 = a1, a0 + a1
        return a1
