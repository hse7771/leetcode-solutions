# Solution for Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        mx_len = 0
        start = 0
        for i in range(len(s)):
            if s[i] in used:
                start = max(start, used[s[i]] + 1)
            used[s[i]] = i
            mx_len = max(mx_len, i - start + 1)
        return mx_len


# Naive solution. Hash table, removal elements one by one, slightly less efficient than approach above
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         used = set()
#         mx_len = 0
#         start = 0
#         for i in range(len(s)):
#             if s[i] in used:
#                 while s[start] != s[i]:
#                     used.remove(s[start])
#                     start += 1
#                 start += 1
#             used.add(s[i])
#             mx_len = max(mx_len, i - start + 1)
#         return mx_len
