# Solution for Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def explode(s, left, right):
            n = len(s)
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        left_answer, right_answer = 0, 0
        for i in range(1, len(s)):
            left1, right1 = explode(s, i - 1, i)
            left2, right2 = explode(s, i, i)
            if right1 - left1 > right_answer - left_answer:
                left_answer, right_answer = left1, right1
            if right2 - left2 > right_answer - left_answer:
                left_answer, right_answer = left2, right2
        return s[left_answer: right_answer + 1]
