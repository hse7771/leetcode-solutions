
# 🧠 First Unique Character In A String

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/description/)

---

## 📝 Intuition

Hash input string and perform basic traversal. Use python dict insert order memory property.

## 🔍 Approach

1. Traverse the string once and build a hash map:
   - If a character is seen for the first time, store its index.
   - If it’s seen again, overwrite its value with `-1` to mark it non-unique.
2. Because Python dicts preserve insertion order (by first insertion), a second iteration over the map finds the earliest character whose value is not `-1`.
3. Return that stored index, or `-1` if none exist.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input string, to store it, and up to $26$ elements in the hash table, so $O(1)$.

---

## 🧩 Code

```python3 []
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}
        for i in range(len(s)):
            if s[i] not in hash_table:
                hash_table[s[i]] = i
            else:
                hash_table[s[i]] = -1
        answer = -1
        for ch, idx in hash_table.items():
            if idx != -1:
                answer = idx
                break
        return answer
```

