# Solution for Make The String Great

# Stack approach (Efficient)
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1].lower() == s[i].lower() and stack[-1] != s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)


# List approach (Naive)
# Worst case O(N^2) (all elements are shifted every time)
# class Solution:
#     def makeGood(self, s: str) -> str:
#         i = 0
#         s_list = list(s)
#         while i < len(s_list) - 1:
#             if s_list[i] != s_list[i + 1] and s_list[i].lower() == s_list[i + 1].lower():
#                 s_list.pop(i)
#                 s_list.pop(i)
#                 i = max(i - 1, 0)
#             else:
#                 i += 1
#         return "".join(s_list)
