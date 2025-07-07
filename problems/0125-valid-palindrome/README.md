
# 🧠 Valid Palindrome

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/valid-palindrome/description/)

---

## 📝 Intuition

Check for palindrome by comparing characters from both ends towards the center.

## 🔍 Approach

- Use two pointers (`l` at the start, `r` at the end).
- Move both pointers towards each other:
  - Skip characters that are not alphanumeric.
  - Compare the characters (in lowercase) at both pointers.
  - If they do not match, return `False`.
- Continue until the pointers meet or cross.
- If no mismatch is found, return `True`.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input string, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
```

