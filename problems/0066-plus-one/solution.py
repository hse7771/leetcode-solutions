# Solution for Plus One
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                return digits
        return digits


# Alternative approach, same efficiency
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         decimal_place = 1
#         for i in range(len(digits) - 1, -1, -1):
#             digits[i] += decimal_place
#             decimal_place = digits[i] // 10
#             digits[i] %= 10
#         if decimal_place == 1:
#             digits.insert(0, 1)
#         return digits
