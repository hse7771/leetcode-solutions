
# 🧠 Roman To Integer

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/roman-to-integer/description/)

---

## 📝 Intuition

Use hash table and perform basic string traversal.

## 🔍 Approach

1. Initialize a dictionary mapping Roman numerals (including subtractive pairs) to their integer values.
2. Initialize the result with the value of the first character.
3. Loop through the string starting from the second character:
   - Add the value of the current symbol to the result.
   - Check if the previous and current symbols together form a subtractive pair (e.g. "IV", "IX"):
     - If so, subtract twice the value of the previous symbol to adjust for the overcount.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the lengths of the input string.


- **Space Complexity:** $O(1)$  
To store constant size dictionary.

---

## 🧩 Code

```python3 []
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_arabic = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        arabic = roman_to_arabic[s[0]]
        for i in range(1, len(s)):
            arabic += roman_to_arabic[s[i]]
            roman_digit = s[i - 1] + s[i]
            if roman_digit in roman_to_arabic:
                arabic -= (2 * roman_to_arabic[s[i - 1]])
        return arabic
```

