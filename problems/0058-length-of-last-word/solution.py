# Solution for Length Of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n_last = 0
        cur = 0
        for char in s:
            if char.isalpha():
                cur += 1
            else:
                if cur != 0:
                    n_last = cur
                cur = 0
        if cur != 0:
            n_last = cur
        return n_last


# Easy solution using python advanced built-in features
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])
