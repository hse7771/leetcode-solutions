
# 🧠 Longest Palindromic Substring

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/description/)

---

## 📝 Intuition

A palindrome mirrors around its center. Every palindrome is defined by either:
- an **odd** center at some index `i`, or
- an **even** center between indices `(i-1, i)`.

If we expand outward from each possible center while the characters match, 
we can find the longest palindrome in one pass over all centers.

## 🔍 Approach

1. Define a helper `explode(s, left, right)` that expands while `s[left] == s[right]` 
and stays in bounds, returning the final inclusive `(L, R)` of the palindrome.
2. Track the best answer window `(left_answer, right_answer)` seen so far.
3. For each index `i`:
   - Expand around the **even** center `(i-1, i)`.
   - Expand around the **odd** center `(i, i)`.
   - Update the best window if either expansion is longer than the current best.
4. Return `s[left_answer : right_answer + 1]`.

## 📊 Complexity

- **Time Complexity:** $O(N^2)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input string, to store it.

---

## 🧩 Code

```python3 []
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
        return s[left_answer : right_answer + 1]
```

