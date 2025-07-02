# Solution for Sqrt(X)

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while right - left > 1:
            middle = (right + left) // 2
            if x < middle * middle:
                right = middle
            else:
                left = middle
        return left
