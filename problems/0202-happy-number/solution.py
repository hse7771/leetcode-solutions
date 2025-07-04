# Solution for Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        happy_number = n
        used_numbers = set()
        while happy_number != 1:
            num_copy = happy_number
            if happy_number in used_numbers:
                break
            used_numbers.add(happy_number)
            happy_number = 0
            while num_copy != 0:
                happy_number += (num_copy % 10) * (num_copy % 10)
                num_copy //= 10
        return happy_number == 1
