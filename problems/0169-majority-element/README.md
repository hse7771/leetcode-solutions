
# 🧠 Majority Element

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/majority-element/description/)

---

## 📝 Intuition

Use either hash table with $O(N)$ space complexity or use a more elegant **Boyer–Moore Majority Vote** Algorithm.

## 🔍 Approach

- Initialize `key` as the potential majority element and `count` as 0.
- Iterate through the array:
  - If `count` is 0, set the current element as the new `key`.
  - If the current element equals `key`, increment `count`.
  - Otherwise, decrement `count`.
- At the end, `key` will be the majority element due to the Boyer–Moore Majority Vote Algorithm.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input array.


- **Space Complexity:** $O(1)$  
No extra space is used.

---

## 🧩 Code

```python3 []
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == key:
                count += 1
            elif count == 0:
                key = nums[i]
                count += 1
            else:
                count -= 1
        return key
```

