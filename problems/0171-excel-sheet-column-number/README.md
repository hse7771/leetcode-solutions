
# 🧠 Excel Sheet Column Number

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/excel-sheet-column-number/description/)

---

## 📝 Intuition

Use the idea of number systems.

## 🔍 Approach

- Treat the string as a number in base 26 where:
  - 'A' maps to 1, 'B' to 2, ..., 'Z' to 26.
- Iterate through each character from left to right:
  - For each character, multiply its value by 26 raised to its positional power.
- Accumulate the result to get the final column number.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(1)$  
Memory needed only for few variables.

---

## 🧩 Code

```python3 []
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        correction = 64
        base = 26
        num = 0
        n = len(columnTitle)
        for i in range(n):
            num += (ord(columnTitle[i]) - correction) * base**(n - 1 - i)
        return num
```

