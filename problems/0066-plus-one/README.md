
# 🧠 Plus One

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/plus-one/description/)

---

## 📝 Intuition

Basic array inverse traversal.

## 🔍 Approach

1. Traverse the array from the last digit to the first.
2. Add 1 to the current digit.
3. If the digit becomes less than $10$ after addition, return the array.
4. If the digit becomes $10$, set it to $0$ and continue to the next digit on the left.
5. If all digits are processed and there is still a carry, insert $1$ at the beginning of the array.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(N)$
$N$ is the number of elements in the input array, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                return digits
        return digits
```

