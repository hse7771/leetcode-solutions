
# 🧠 Group Anagrams

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/group-anagrams/description/)

---

## 📝 Intuition

Anagrams share the same **multiset of characters**. If we convert each string to a **canonical form** 
(e.g., its sorted characters), all anagrams map to the same key and can be grouped together in a hash map.

## 🔍 Approach

1. Iterate over each string `s` in `strs`.
2. Build a key for the anagram class:  
   - **This solution:** `key = tuple(sorted(s))`.
   - **Alternative:** `key = tuple(counts_26(s))` (character frequencies).
3. Append `s` into a hash map `key -> list of strings`.
4. Return all the grouped lists.

## 📊 Complexity

- **Time Complexity:** $O(N \cdot L logL)$  
$N$ is the number of strings and $L$ is the average string length.


- **Space Complexity:** $O(N · L)$  
$N$ is the number of strings and $L$ is the average string length,
to store them in groups and their keys (overall output size dominates).

---

## 🧩 Code

```python3 []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for s in strs:
            key = tuple(sorted(s))
            hash_table.setdefault(key, []).append(s)
        return list(hash_table.values())
```

