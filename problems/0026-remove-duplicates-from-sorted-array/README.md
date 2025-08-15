
# 🧠 Remove Duplicates From Sorted Array

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

---

## 📝 Intuition

Since the array is sorted, duplicates will be adjacent.  
Two pointers can be used: one to read elements (`i`) and one to write unique elements (`write`).  

## 🔍 Approach

1. Initialize `write = 0` as the index to place the next unique element.
2. Iterate through the array starting from index `1`:
   - If `nums[i]` is different from `nums[write]`:
     - Increment `write`.
     - Assign `nums[write] = nums[i]` to overwrite the duplicate.
3. After traversal, the first `write + 1` elements are the unique elements.
4. Return `write + 1` as the count of unique elements.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is number of elements in the input array.


- **Space Complexity:** $O(N)$  
$N$ is number of elements in the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for i in range(1, len(nums)):
            if nums[write] != nums[i]:
                write += 1
                nums[write] = nums[i]
        return write + 1
```

