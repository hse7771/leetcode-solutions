# Solution for String To Integer (Atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i].isspace():
            i += 1
        if i == len(s):
            return 0

        sign = 1
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                sign = -1
            i += 1

        number = 0
        while i < len(s) and s[i].isdigit():
            number = number * 10 + int(s[i])
            i += 1

        number *= sign

        int_min, int_max = -2**31, 2**31 - 1
        if number < int_min:
            return int_min
        if number > int_max:
            return int_max

        return number
