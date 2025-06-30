# Solution for Palindrome Number


# Efficient
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_copy = x
        x_recovery = 0
        while x_copy != 0:
            x_recovery = x_recovery * 10 + x_copy % 10
            x_copy //= 10
        return x == x_recovery


# Naive
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         x_copy = x
#         n = 0
#         while x_copy != 0:
#             x_copy //= 10
#             n += 1
#         for i in range(n // 2):
#             if x // 10**i % 10 != x // 10**(n-i-1) % 10:
#                 return False
#         return True

# String conversion
# Convert to string and use slices
