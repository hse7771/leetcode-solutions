
# 🧠 Longest Common Prefix

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/longest-common-prefix/description/)

---

## 📝 Intuition

Perform basic string array and string traversal.

## 🔍 Approach

1. Find the shortest string

2. Iterate through each character position `i` 
   - For each character in the shortest string:
     - Compare it with the character at the same position in all other strings.
     - If a mismatch is found at any position:
       - Return the substring up to that index as the common prefix.

3. Return the full shortest string if no mismatches are found

## 📊 Complexity

- **Time Complexity:** $O(N \cdot M)$  
$N$ is the number of strings in $strs$ and $M$ is the length of the _shortest_ string.


- **Space Complexity:** $O(N \cdot M)$  
$N$ is the number of strings in $strs$ and $M$ is the length of the _longest_ string, to store strings. 

---

## 🧩 Code

```python3 []
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = min(strs, key=len)
        for i in range(len(lcp)):
            for s in strs:
                if s[i] != lcp[i]:
                    return lcp[:i]
        return lcp
```

