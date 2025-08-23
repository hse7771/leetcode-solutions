
# 🧠 Jump Game

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/jump-game/description/)

---

## 📝 Intuition

Perform basic array traversal with tracking.

## 🔍 Approach

1. Initialize `i = 0`, `steps = nums[0]`.
2. While `i < n - 1` and `steps != 0`:
   - Move forward: `i += 1`, `steps -= 1`.
   - Refill reach: `steps = max(steps, nums[i])`.
3. Return `i == n - 1`.

This greedily maintains the best possible remaining reach at each position.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(N)$  
$N$ is the number of elements in the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        steps = nums[i]
        while i < n - 1 and steps != 0:
            i += 1
            steps -= 1
            steps = max(steps, nums[i])
        return i == n - 1
```

