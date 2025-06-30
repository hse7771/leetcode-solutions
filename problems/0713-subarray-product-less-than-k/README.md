
# 🧠 Subarray Product Less Than K

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/description/)

---

## 📝 Intuition

Use sliding window.

## 🔍 Approach

1. **Initialize pointers:**
   - `p_i` = window start (left)
   - `i` = window end (right)

2. **Accumulate the product** as the window extends to the right.

3. **If the product becomes $\geq k$**, move the left pointer (`p_i`) right and divide out the leftmost value until the product is valid (i.e., $<$ k) or the window collapses.

4. **For every position $i$**, the number of valid subarrays ending at $i$ is `i - p_i + 1`.

   - **Why?** Because all subarrays `[p_i, i]`, `[p_i+1, i]`, ..., `[i, i]` are guaranteed to have product $< k$.

5. **Continue for all $i$**, and sum the counts.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input array.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input array to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        p_i = 0
        count = 0
        n = len(nums)
        for i in range(n):
            p *= nums[i]
            while p >= k and p_i <= i:
                p //= nums[p_i]
                p_i += 1
            count += (i - p_i + 1)
        return count

```
