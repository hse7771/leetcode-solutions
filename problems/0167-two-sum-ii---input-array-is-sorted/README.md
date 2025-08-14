
# 🧠 Two Sum Ii   Input Array Is Sorted

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

---

## 📝 Intuition

Perform basic 2 pointers array traversal.

## 🔍 Approach

1. Initialize two pointers: `left = 0` and `right = len(numbers) - 1`.
2. Compute `s = numbers[left] + numbers[right]`.
3. If `s == target`, return the 1-indexed positions `[left + 1, right + 1]`.
4. If `s > target`, decrement `right` to reduce the sum.
5. If `s < target`, increment `left` to increase the sum.
6. Repeat until the pair is found (the problem guarantees exactly one solution).

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input array.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while (s := numbers[left] + numbers[right]) != target:
            if s > target:
                right -= 1
            else:
                left += 1
        answer = [left + 1, right + 1]
        return answer
```

