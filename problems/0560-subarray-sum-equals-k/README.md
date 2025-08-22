
# 🧠 Subarray Sum Equals K

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/description/)

---

## 📝 Intuition

Use prefix sum idea and hashing array approach to speed up search operations.

## 🔍 Approach

Scan left to right and maintain:
- `accumulating_sum` — current prefix sum,
- `hash_table` — counts of seen prefix sums (seed with `{0: 1}` to allow subarrays starting at index 0),
- `count` — number of subarrays with sum `k`.

For each element:
1. Update `accumulating_sum += nums[i]`.
2. Add `hash_table.get(accumulating_sum - k, 0)` to `count`.
3. Increment `hash_table[accumulating_sum]`.

Return `count`.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(N)$  
$N$ is the number of elements in the input array, to store it.
Up to $O(N)$ space for the hash table (if all prefix sums are distinct).

---

## 🧩 Code

```python3 []
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        accumulating_sum = 0
        hash_table = {0: 1}
        count = 0
        for i in range(len(nums)):
            accumulating_sum += nums[i]
            target = accumulating_sum - k
            count += hash_table.get(target, 0)
            hash_table[accumulating_sum] = hash_table.get(accumulating_sum, 0) + 1
        return count
```

