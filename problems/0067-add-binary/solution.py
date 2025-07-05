# Solution for Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        extra_dec_place = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or extra_dec_place != 0:
            r = extra_dec_place
            if i >= 0:
                r += int(a[i])
                i -= 1
            if j >= 0:
                r += int(b[j])
                j -= 1
            result.append(str(r % 2))
            extra_dec_place = r // 2
        return "".join(result)[::-1]
