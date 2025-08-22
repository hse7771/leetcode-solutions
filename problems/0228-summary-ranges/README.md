
# 🧠 Summary Ranges

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/summary-ranges/description/)

---

## 📝 Intuition

Perform basic array traversal and some kind of 2 pointers idea.

## 🔍 Approach

1. If `nums` is empty, return `[]`.
2. Initialize `start = end = nums[0]`.
3. Iterate `i = 1..n-1`:
   - If `nums[i] == end + 1`, extend the current run: `end = nums[i]`.
   - Otherwise, append the finished run to the answer:
     - If `start == end` → append `str(start)`.
     - Else → append `f"{start}->{end}"`.
     Then start a new run at `start = end = nums[i]`.
4. After the loop, append the final run in the same way.
5. Return the collected list of range strings.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(N)$  
$N$ is the number of elements in the input array, to store it.
And also up to $O(N)$ for storing the answer, as sequence can be like $x, x + 2, x + 4$.

---

## 🧩 Code

```python3 []
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 == end:
                end = nums[i]
            else:
                if start != end:
                    result.append(f"{start}->{end}")
                else:
                    result.append(str(start))
                start = end = nums[i]
        if start != end:
            result.append(f"{start}->{end}")
        else:
            result.append(str(start))
        return result
```

