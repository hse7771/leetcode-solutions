
# 🧠 String To Integer (Atoi)

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/string-to-integer-atoi/description/)

---

## 📝 Intuition

Perform string traversal.

## 🔍 Approach

1. Skip leading whitespaces.
2. Determine the optional sign (`+` or `-`).
3. Parse consecutive digit characters into an integer.
4. Apply the sign to the number.
5. Clamp the result to the 32-bit signed integer range.
6. Return the final result.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input string, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while  i < len(s) and s[i].isspace():
            i += 1
        if i == len(s):
            return 0

        sign = 1
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                sign = -1
            i += 1

        number = 0
        while i < len(s) and s[i].isdigit():
            number = number * 10 + int(s[i])
            i += 1

        number *= sign

        int_min, int_max = -2**31, 2**31 - 1
        if number < int_min:
            return int_min
        if number > int_max:
            return int_max

        return number
```

