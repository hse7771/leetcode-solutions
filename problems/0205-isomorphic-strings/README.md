
# 🧠 Isomorphic Strings

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/isomorphic-strings/description/)

---

## 📝 Intuition

Use hash table.

## 🔍 Approach


1. Initialize a hash table to store the mapping from characters in `s` to characters in `t`, and a set to keep track of 
already mapped characters in `t`.
2. Loop through the two strings in parallel:
    - If the character from `s` has no mapping:
        - If the character from `t` is already mapped, return `False` (no two characters in `s` can map to the same character in `t`).
        - Otherwise, create the mapping and record the character from `t` as mapped.
    - If a mapping exists, check that it matches the current character from `t`; if not, return `False`.
3. If the loop completes, the strings are isomorphic—return `True`.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input strings, not total.


- **Space Complexity:** $O(N)$  
Up to $N$ mappings may be stored in the hash table and set.

---

## 🧩 Code

```python3 []
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hast_table = {}
        hashed_chars = set()
        for s_ch, t_ch in zip(s, t):
            if s_ch not in hast_table:
                if t_ch in hashed_chars:
                    return False
                hast_table[s_ch] = t_ch
                hashed_chars.add(t_ch)
            else:
                if hast_table[s_ch] != t_ch:
                    return False
        return True
```

