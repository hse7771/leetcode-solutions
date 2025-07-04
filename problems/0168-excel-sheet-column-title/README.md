
# 🧠 Excel Sheet Column Title

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/excel-sheet-column-title/description/)

---

## 📝 Intuition

Use the idea of number systems.

## 🔍 Approach

- Treat the problem as a base-26 conversion, similar to converting a number to another numeral system.
- Adjust by subtracting 1 from `columnNumber` before each modulo to handle Excel's 1-based indexing.
- Convert each remainder to a character by adding it to the ASCII value of 'A' minus 1.
- Append each character to a list and reverse it at the end to obtain the correct order.

## 📊 Complexity

- **Time Complexity:** $O(logN)$  
$N$ is the input number.


- **Space Complexity:** $O(logN)$  
Where $logN$ is the length of the output string.

---

## 🧩 Code

```python3 []
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = []
        base = 26
        correction = 64
        while columnNumber > 0:
            columnNumber -= 1
            part = columnNumber % base
            translated_part = chr(part + correction + 1)
            s.append(translated_part)
            columnNumber //= base
        return "".join(s[::-1])
```

