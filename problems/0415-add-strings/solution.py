# Solution for Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        result = []
        offset = ord("0")
        while i >= 0 or j >= 0 or carry == 1:
            dig1 = ord(num1[i]) - offset if i >= 0 else 0
            dig2 = ord(num2[j]) - offset if j >= 0 else 0
            s = dig1 + dig2 + carry
            result.append(str(s % 10))
            carry = s // 10
            i -= 1
            j -= 1
        return "".join(result[::-1])
