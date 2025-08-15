
# 🧠 Is Subsequence

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/is-subsequence/description/)

---

## 📝 Intuition

Perform basic 2 pointers arrays simultaneous traversal.

## 🔍 Approach

1. Initialize two pointers `i = 0` for `s` and `j = 0` for `t`.
2. While both pointers are within bounds:
   - If `s[i] == t[j]`, increment `i` (we matched one more character of `s`).
   - Always increment `j` to move forward in `t`.
3. After traversal, if `i == len(s)`, it means all characters in `s` were matched in order within `t`, so return `True`.
4. Otherwise, return `False`.

## 📊 Complexity

- **Time Complexity:** $O(\min(N, M))$  
$N$ and $M$ are lengths of the input strings.


- **Space Complexity:** $O(N + M)$  
$N$ and $M$ are lengths of the input strings, to store them.

---

## 🧩 Code

```python3 []
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
```

