
# 🧠 Swap Adjacent In Lr String

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/swap-adjacent-in-lr-string/description/)

---

## 📝 Intuition

Perform string 2 pointer traversal.

## 🔍 Approach

1. Use two pointers (`i` for `start`, `j` for `result`) to traverse both strings simultaneously.
2. Skip all 'X' characters in both strings, since 'X' can be freely swapped.
3. For each non-'X' character:
   - If the current characters in `start` and `result` differ, return `False`.
   - If the character is 'L', ensure it never moves to the right (i.e., `i` should be ≥ `j`).
   - If the character is 'R', ensure it never moves to the left (i.e., `i` should be ≤ `j`).
4. Increment both pointers and continue.
5. After traversal, confirm both pointers have reached the end; otherwise, return `False`.
6. If all checks pass, return `True`.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of input strings.


- **Space Complexity:** $O(N)$  
Where $N$ is the length of input strings to store them.

---

## 🧩 Code

```python3 []
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        i, j = 0, 0
        n = len(start)
        while i < n and j < n:
            if start[i] != "X" and result[j] != "X":
                if start[i] != result[j]:
                    return False
                elif start[i] == "L" and i < j:
                    return False
                elif start[i] == "R" and i > j:
                    return False
                i += 1
                j += 1
            while i < n and start[i] == "X":
                i += 1
            while j < n and result[j] == "X":
                j += 1
        return i == j
```

