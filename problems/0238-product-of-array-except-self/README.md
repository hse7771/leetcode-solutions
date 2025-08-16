
# 🧠 Product Of Array Except Self

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/description/)

---

## 📝 Intuition

We need the product of all elements except the current one, without using division.  
A naive solution would compute the product for each index separately ($O(N^2)$).  
Instead, we can precompute prefix products (from the left) and suffix products (from the right) and combine them.

## 🔍 Approach

1. Initialize a `result` array of size `n` with all `1`s.  
2. Traverse from left to right:
   - For each index `i`, store the product of all numbers before `i`.  
   - Maintain a running product `left`.
3. Traverse from right to left:
   - Multiply `result[i]` by the product of all numbers after `i`.  
   - Maintain a running product `right`.
4. The result array now contains the product of all numbers except itself.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input array.


- **Space Complexity:** $O(N)$ 
$N$ is the size of the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left = nums[0]
        for i in range(1, n):
            result[i] = left
            left *= nums[i]
        right = nums[n - 1]
        for j in range(n - 2, -1, -1):
            result[j] *= right
            right *= nums[j]

        return result
```

