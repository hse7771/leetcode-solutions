
# 🧠 Two Sum

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/two-sum/description/)

---

## 📝 Intuition

Use hash table and perform array traversal.

## 🔍 Approach

- Initialize an empty hash table to store previously seen numbers and their indices.
- Traverse the array:
  - For each element, compute the complement (target - current element).
  - If the complement exists in the hash table, a solution is found; return both indices.
  - Otherwise, store the current element and its index in the hash table.
- This ensures that each lookup and insertion is done in constant time.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(N)$  
$N$ is the number of elements in the input array, to store it and to store hash table.

---

## 🧩 Code

```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        answer = []
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hash_table:
                answer = [i, hash_table[key]]
                break
            if nums[i] not in hash_table:
                hash_table[nums[i]] = i
        return answer
```

