# Solution for Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        correction = 64
        base = 26
        num = 0
        n = len(columnTitle)
        for i in range(n):
            num += (ord(columnTitle[i]) - correction) * base**(n - 1 - i)
        return num
