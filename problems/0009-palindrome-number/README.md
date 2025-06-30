
# 🧠 Palindrome Number

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/palindrome-number/description/)

---

## 📝 Intuition
Need to avoid string typecasting.

## 🔍 Approach
Use integer division and remainders.

## 📊 Complexity

- **Time Complexity:**
$O(logN)$  
$N$ is the input number ($x$).


- **Space Complexity:**
$O(1)$  
No additional memory is required.

---

## 🧩 Code

```python3 []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_copy = x
        x_recovery = 0
        while x_copy != 0:
            x_recovery = x_recovery * 10 + x_copy % 10
            x_copy //= 10
        return x == x_recovery
```
