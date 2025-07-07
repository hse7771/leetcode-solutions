
# 🧠 Longest Substring Without Repeating Characters

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

---

## 📝 Intuition

Use hash table and single traversal.

## 🔍 Approach

- Use a hash table (`used`) to store the most recent index of each character seen.
- Initialize `mx_len` for the maximum substring length and `start` as the left boundary of the current substring window.
- Traverse the string from left to right:
  - If the current character has been seen and its last occurrence is at or after the current window start, move `start`
    to one position after its last occurrence (ensuring all characters in the window remain unique).
  - Update the character's latest index in the hash table.
  - Calculate the current window length (`i - start + 1`) and update `mx_len` if this window is longer.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input string to store it. Let $K$ be the number of letters in the alphabet, then to store 
the hash table constant space is sufficient.

---

## 🧩 Code

```python3 []
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
```

