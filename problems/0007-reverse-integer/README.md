
# 🧠 Reverse Integer

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/reverse-integer/description/)

---

## 📝 Intuition

Use integer division and modulus to reverse digits without string conversion.

## 🔍 Approach

1. Determine the sign of the input number.
2. Take the absolute value and reverse it digit by digit using modulus and integer division:
   - Extract the last digit using `% 10`.
   - Append it to the reversed number by multiplying the current reversed number by `10` and adding the digit.
   - Remove the last digit from the original number using `// 10`.
3. Apply the original sign to the reversed number.
4. Check if the reversed number is within the 32-bit signed integer range:
   - If not, return `0`.
5. Return the reversed number.

## 📊 Complexity

- **Time Complexity:** $O(logN)$  
$N$ is the input number.


- **Space Complexity:** $O(1)$  
Only one integer needs to be stored.

---

## 🧩 Code

```python3 []
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        num = 0
        while x != 0:
            num = num * 10 + x % 10
            x //= 10
        num *= sign

        int_min, int_max = -2 ** 31, 2 ** 31 - 1
        if num < int_min or num > int_max:
            return 0
        return num
```

