
# 🧠 Sqrt(X)

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/sqrtx/description/)

---

## 📝 Intuition

Use binary search algorithm.

## 🔍 Approach

1. Initialize search boundaries `left = 0` and `right = x + 1`.
2. While `right - left > 1`:
   - Calculate `middle`.
   - If `middle * middle` is greater than `x`, move `right` to `middle`.
   - Otherwise, move `left` to `middle`.
3. Return `left` as it is the largest integer such that `left * left <= x`.

## 📊 Complexity

- **Time Complexity:** $O(logN)$  
$N$ is the input number.


- **Space Complexity:** $O(1)$  
To store only 1 input number.

---

## 🧩 Code

```python3 []
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while right - left > 1:
            middle = (right + left) // 2
            if x < middle * middle:
                right = middle
            else:
                left = middle
        return left
```

