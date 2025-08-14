
# 🧠 Missing Number

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/missing-number/description/)

---

## 📝 Intuition

Use arithmetic progression and basic array traversal with sum accumulation.

## 🔍 Approach

1. Let `n = len(nums)`. The full range should be the integers `0..n`.
2. Compute the expected sum using Gauss’s formula: `expected = n * (n + 1) // 2`.
3. Compute the actual sum: `actual = sum(nums)`.
4. The answer is `expected - actual`.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array. Single pass to compute `sum(nums)`.


- **Space Complexity:** $O(N)$  
$N$ is the number of elements in the input array to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (1 + n) * n // 2
        return s - sum(nums)
```

