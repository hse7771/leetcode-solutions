
# 🧠 Single Number

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/single-number/description/)

---

## 📝 Intuition

Perform basic array traversal and use XOR idea.

## 🔍 Approach

Scan the array once while maintaining a running XOR:
- Initialize an accumulator with the first element and XOR it with each subsequent element.
- Because equal numbers cancel, the accumulator ends up being the unique number.

This works for negative and positive integers alike and uses constant extra space.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input array.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = nums[0]
        for i in range(1, len(nums)):
            x ^= nums[i]
        return x
```

