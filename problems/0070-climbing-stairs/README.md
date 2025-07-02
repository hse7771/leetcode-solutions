
# 🧠 Climbing Stairs

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/climbing-stairs/description/)

---

## 📝 Intuition

Use basic dynamic programming.

## 🔍 Approach

1. Recognize that climbing stairs is equivalent to the Fibonacci sequence:
   - To reach step `n`, you can come from step `n-1` or step `n-2`.
2. Initialize two variables to store the number of ways to reach the two previous steps.
3. Iterate from step `1` to `n-1`, updating the counts for each step based on the sum of the previous two.
4. Return the final count as the total number of ways to climb `n` stairs.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the input number.


- **Space Complexity:** $O(1)$  
Constant memory allocation for any input.

---

## 🧩 Code

```python3 []
class Solution:
    def climbStairs(self, n: int) -> int:
        a0, a1 = 1, 1
        for step in range(1, n):
            a0, a1 = a1, a0 + a1
        return a1
```

