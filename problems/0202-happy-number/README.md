
# 🧠 Happy Number

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/happy-number/description/)

---

## 📝 Intuition

Implement happy number algorithm and use hash table to track the endless loop.

## 🔍 Approach

- Initialize a variable to track the current number (`happy_number`) and a set (`used_numbers`) to store previously seen numbers.
- While the current number is not `1`:
  - If it is already in `used_numbers`, a cycle is detected and the number is not happy.
  - Otherwise, add it to `used_numbers`.
  - Calculate the sum of the squares of its digits and update `happy_number`.
- Return `True` if the process ends with `happy_number == 1`, otherwise return `False`.

## 📊 Complexity

- **Time Complexity:** $O(K)$  
Where $K$ is the number of unique intermediate sums before repetition or reaching $1$. Since possible sums are limited 
(maximum sum is $9^2 \times$ number of digits), this is effectively bounded and does not depend on $N$.


- **Space Complexity:** $O(K)$  
For storing previously seen numbers to detect cycles.

---

## 🧩 Code

```python3 []
class Solution:
    def isHappy(self, n: int) -> bool:
        happy_number = n
        used_numbers = set()
        while happy_number != 1:
            num_copy = happy_number
            if happy_number in used_numbers:
                break
            used_numbers.add(happy_number)
            happy_number = 0
            while num_copy != 0:
                happy_number += (num_copy % 10) * (num_copy % 10)
                num_copy //= 10
        return happy_number == 1
```

