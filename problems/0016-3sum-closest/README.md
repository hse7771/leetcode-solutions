
# 🧠 3Sum Closest

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/3sum-closest/description/)

---

## 📝 Intuition

Use two pointers approach to efficiently iterate over all pair combinations. 
Then add another outer loop to iterate over all possible triplets.

## 🔍 Approach

1. Sort the array to allow the use of the two-pointer technique.
2. Iterate through the array with index `i` representing the first element of the triplet.
3. For each `i`, set two pointers:
   - `l` (left) starting at `i + 1`
   - `r` (right) starting at the end of the array.
4. Compute the sum of the three elements (`nums[i] + nums[l] + nums[r]`) and its difference from `target`.
5. If the difference is smaller than the current best, update the closest sum and the minimal difference.
6. Move the pointers:
   - If the sum is greater than `target`, decrement `r` to try a smaller sum.
   - Otherwise, increment `l` to try a larger sum.
7. Continue until all triplets are checked, then return the closest sum found.

## 📊 Complexity

- **Time Complexity:** $O(N^2)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(N)$  
$N$ is the number of element in the array, to store it, and additional space for sorting operation.

---

## 🧩 Code

```python3 []
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = None
        diff_closest = 10**8
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(target - s)
                if diff < diff_closest:
                    diff_closest = diff
                    closest_sum = s
                if s > target:
                    r -= 1
                else:
                    l += 1
        return closest_sum
```

