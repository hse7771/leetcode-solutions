
# 🧠 Find First And Last Position Of Element In Sorted Array

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)

---

## 📝 Intuition

Use basic binary search algorithm with modification to find the left and right boundaries.

## 🔍 Approach

1. Perform two modified binary searches:
   - **First search:** Find the leftmost (first) occurrence of the target by moving `right` when `nums[mid] >= target`.
   - **Second search:** Find the rightmost (last) occurrence of the target by moving `left` when `nums[mid] <= target`.
2. Return the indices of the left and right boundaries as the result.

## 📊 Complexity

- **Time Complexity:** $O(logN)$  
$N$ is the length of the input array.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_boundary, right_boundary = -1, -1
        if not nums:
            return [left_boundary, right_boundary]

        left, right = -1, len(nums)
        while right - left > 1:
            middle = (right + left) // 2
            if target <= nums[middle]:
                right = middle
            else:
                left = middle
        if 0 <= right < len(nums) and nums[right] == target:
            left_boundary = right

        left, right = left_boundary - 1, len(nums)
        while right - left > 1:
            middle = (right + left) // 2
            if target < nums[middle]:
                right = middle
            else:
                left = middle
        if 0 <= right - 1 < len(nums) and nums[right - 1] == target:
            right_boundary = right - 1

        return [left_boundary, right_boundary]
```

