# Solution for Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = []
        base = 26
        correction = 64
        while columnNumber > 0:
            columnNumber -= 1
            part = columnNumber % base
            translated_part = chr(part + correction + 1)
            s.append(translated_part)
            columnNumber //= base
        return "".join(s[::-1])
