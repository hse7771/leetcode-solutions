
# 🧠 Longest Subarray Of 1'S After Deleting One Element

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/)

---

## 📝 Intuition

Perform basic array traversal, maintaining 2 counters simultaneously.

## 🔍 Approach

1. Use two counters:
   - `cur`: current streak of consecutive 1s.
   - `prev`: streak of consecutive 1s immediately before the most recent 0.
2. Traverse the array:
   - If the current element is 1, increment `cur`.
   - If the current element is 0, set `prev` to `cur` and reset `cur` to 0.
   - After each step, update the result as the sum of `prev + cur`.
3. At the end, if the array contains only 1s (i.e., `mx == len(nums)`), subtract 1 because one element must be deleted.
4. Return the result.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input array.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 0
        prev = cur = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                prev = cur
                cur = 0
            mx = max(mx, prev + cur)
        if mx == len(nums):
            mx -= 1
        return mx
```
