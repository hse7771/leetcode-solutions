# Solution for Find The Index Of The First Occurrence In A String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_n = len(needle)
        for i in range(len(haystack) - needle_n + 1):
            fl = True
            for j in range(needle_n):
                if needle[j] != haystack[i + j]:
                    fl = False
                    break
            if fl:
                return i
        return -1


# Using Python built-in methods
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)
