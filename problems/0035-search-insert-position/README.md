
# 🧠 Search Insert Position

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/search-insert-position/description/)

---

## 📝 Intuition

Basic binary search algorithm.

## 🔍 Approach


1. Implement binary search to find the leftmost index where the element is greater than or equal to the target.
2. After the loop, `right` will be the correct insert position (or index of the found element).

## 📊 Complexity

- **Time Complexity:** $O(logN)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(N)$  
$N$ is the number of elements in the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while right - left > 1:
            middle = (right + left) // 2
            if target <= nums[middle]:
                right = middle
            else:
                left = middle
        return right
```

