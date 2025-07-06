
# 🧠 Move Zeroes

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/move-zeroes/description/)

---

## 📝 Intuition

Use tracking pointer idea.

## 🔍 Approach

- Initialize a pointer `cur_insert` to track the position where the next nonzero element should be placed.
- Traverse the array:
  - If the current element is nonzero, place it at `cur_insert` and increment `cur_insert`.
- After processing all elements, fill the remaining positions in the array (from `cur_insert` to the end) with zeros.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(1)$  
No extra memory needed.

---

## 🧩 Code

```python3 []
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cur_insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur_insert] = nums[i]
                cur_insert += 1
        for j in range(cur_insert, len(nums)):
            nums[j] = 0
```

