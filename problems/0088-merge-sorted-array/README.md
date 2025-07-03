
# 🧠 Merge Sorted Array

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)

---

## 📝 Intuition

Perform basic array inverse traversal.

## 🔍 Approach

1. Initialize three pointers: 
   - `i` to the last valid element in `nums1` (`m - 1`)  
   - `j` to the last element in `nums2` (`n - 1`)  
   - `k` to the end of `nums1` (`m + n - 1`)

2. Traverse from the end of both arrays: 
   - Compare `nums1[i]` and `nums2[j]`.  
   - Place the larger of the two at index `k` in `nums1`.  
   - Decrement the pointers accordingly (`i` or `j`, and always `k`).

3. Process remaining elements in `nums2`:  
   - If any elements remain in `nums2` after `nums1` is fully processed, copy them to the front of `nums1`.  
   - No need to copy remaining elements from `nums1` since they are already in place.


## 📊 Complexity

- **Time Complexity:** $O(N + M)$  
$N$ is the length of the first input array and $M$ of the second one respectively.


- **Space Complexity:** $O(N + M)$  
$N$ is the length of the first input array and $M$ of the second one respectively, to store them.

---

## 🧩 Code

```python3 []
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        k = n + m - 1
        while i != -1 and j != -1:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # if elements in nums1 left (i) - they are already in place
        while j != -1:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
```

