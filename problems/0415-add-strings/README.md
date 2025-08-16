
# 🧠 Add Strings

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/add-strings/description/)

---

## 📝 Intuition

Perform basic inverse arrays traversal using 2 pointers. Use carry idea and ASCII codes knowledge. 

## 🔍 Approach

1. Set pointers `i = len(num1) - 1` and `j = len(num2) - 1`, and `carry = 0`.
2. While either pointer is valid or there is a non-zero carry:
   - Take `dig1 = digit at num1[i]` if `i >= 0` else `0`.
   - Take `dig2 = digit at num2[j]` if `j >= 0` else `0`.
   - Compute `s = dig1 + dig2 + carry`.
   - Append `s % 10` to the result buffer.
   - Update `carry = s // 10`.
   - Decrement both pointers.
3. Reverse the result buffer and join to form the final string.

## 📊 Complexity

- **Time Complexity:** $O(\max(N, M))$  
$N$ and $M$ are sizes of the input strings.


- **Space Complexity:** $O(N + M)$  
$N$ and $M$ are sizes of the input strings, to store them.

---

## 🧩 Code

```python3 []
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        result = []
        offset = ord("0")
        while i >= 0 or j >= 0 or carry == 1:
            dig1 = ord(num1[i]) - offset if i >= 0 else 0
            dig2 = ord(num2[j]) - offset if j >= 0 else 0
            s = dig1 + dig2 + carry
            result.append(str(s % 10))
            carry = s // 10
            i -= 1
            j -= 1
        return "".join(result[::-1])
```

