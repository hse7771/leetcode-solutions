
# 🧠 Find The Index Of The First Occurrence In A String

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

---

## 📝 Intuition

Perform string traversal or use Python built-in methods.

## 🔍 Approach

1. Iterate through all possible starting indices in `haystack` where `needle` could fit.
2. For each starting index, compare the substring of length `needle` with `needle` itself.
3. If all characters match, return the starting index.
4. If any character does not match, break out of the inner loop and continue with the next starting index.

## 📊 Complexity

- **Time Complexity:** $O(N \cdot M)$  
$N$ and $M$ are lengths of the input strings respectively, as for each starting position, in the worst case, 
it may be needed to compare up to $M$ characters (if every prefix matches, or if the match fails at the last character).


- **Space Complexity:** $O(N+M)$  
$N$ and $M$ are lengths of the input strings respectively, to store them.

---

## 🧩 Code

```python3 []
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
```

