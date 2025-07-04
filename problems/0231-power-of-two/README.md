
# 🧠 Power Of Two

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/power-of-two/description/)

---

## 📝 Intuition

A power of two can be divided by 2 repeatedly until it becomes 1. If at any point it is not divisible by 2 
(except the final 1), it is not a power of two.

## 🔍 Approach

- Check if `n` is zero; if so, return False immediately.
- While `n` is divisible by 2, divide it by 2.
- After the loop, if `n` is reduced to 1, it is a power of two; otherwise, it is not.

## 📊 Complexity

- **Time Complexity:** $O(logN)$  
$N$ is the input number.


- **Space Complexity:** $O(1)$  
Memory is needed only for few variables.

---

## 🧩 Code

```python3 []
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        if n == 1:
            return True
        return False
```

