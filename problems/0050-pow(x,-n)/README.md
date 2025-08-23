
# 🧠 Pow(X, N)

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/powx-n/description/)

---

## 📝 Intuition

Use **exponentiation by squaring**.  
The identities are:

$x^0 = 1$ \
$x^{-n} = \frac{1}{x^n}$ \
$x^n = (x^2)^{n/2}$ (if $n$ even) \
$x^n = x \cdot x^{n-1}$ (if $n$ odd) 

This reduces the exponent by about half each step ⇒ logarithmic recursion depth.

## 🔍 Approach

1. **Base case:** if `n == 0`, return `1`.
2. **Negative exponent:** if `n < 0`, return `1 / myPow(x, -n)`.
3. **Even exponent:** if `n % 2 == 0`, compute `myPow(x * x, n // 2)`.
4. **Odd exponent:** return `x * myPow(x, n - 1)`.

## 📊 Complexity

- **Time Complexity:** $O(log|N|)$  
$N$ is the input degree.


- **Space Complexity:** $O(log|N|)$  
$N$ is the input degree, recursion stack depth.

---

## 🧩 Code

```python3 []
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)
        return x * self.myPow(x, n - 1)
```

