
# 🧠 Continuous Subarray Sum

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/continuous-subarray-sum/description/)

---

## 📝 Intuition

Combine prefix sum, basic array traversal, integer division and hashing on-the-fly ideas.

## 🔍 Approach

1. Initialize a running remainder `s = nums[0] % k`.  
2. Create a hash map `hash_table` storing the first index where each remainder appeared.  
3. Traverse the array:
   - Update `s = (s + nums[i]) % k`.  
   - If this remainder `s` has been seen before at index `j` and the distance `i - j >= 2`, return `True`.  
   - If `s == 0` at any index `i ≥ 1`, return `True` (subarray from start).  
   - Otherwise, record this remainder in the map if not already present.  
4. If the loop ends, return `False`.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(N)$  
$N$ is the number elements in the input array, to store it. 
Up to $O(K)$ for storing hash table, $K$ is the input value to be multiple of.

---

## 🧩 Code

```python3 []
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = nums[0] % k
        hash_table = {s: 0}
        for i in range(1, len(nums)):
            s = (s + nums[i] % k) % k
            r = (s - k) % k
            if r in hash_table and i - hash_table[r] > 1:
                return True
            elif s == 0:
                return True
            if s not in hash_table:
                hash_table[s] = i
        return False
```

