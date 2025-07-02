# Solution for Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        num = 0
        while x != 0:
            num = num * 10 + x % 10
            x //= 10
        num *= sign

        int_min, int_max = -2 ** 31, 2 ** 31 - 1
        if num < int_min or num > int_max:
            return 0
        return num
