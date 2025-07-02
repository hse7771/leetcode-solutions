
# 🧠 Integer To Roman

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/integer-to-roman/description/)

---

## 📝 Intuition

Use mapping of roman integers to arabic ones.

## 🔍 Approach

1. Store all possible Roman numeral values (including subtractive combinations like "IV", "IX", etc.) in descending order.
2. For each value, subtract it from `num` as many times as possible, appending the Roman symbol to the result each time.
3. Continue until `num` is reduced to zero.

## 📊 Complexity

- **Time Complexity:** $O(1)$  
As largest roman number is 3999 (arabic).


- **Space Complexity:** $O(1)$  
To store one number and constant hash table.

---

## 🧩 Code

```python3 []
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numbers = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman_translation = []
        for part in roman_numbers:
            while num >= part:
                num -= part
                roman_translation.append(roman_numbers[part])
        return "".join(roman_translation)
```

