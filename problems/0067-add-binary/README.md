
# 🧠 Add Binary

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/add-binary/description/)

---

## 📝 Intuition

Perform basic string reverse traversal.

## 🔍 Approach

- Initialize two pointers at the end of each string and a variable to store carry.
- Iterate from right to left while either pointer is valid or there is a carry:
  - Add the digits at both pointers (if valid) plus the carry.
  - Append the result modulo 2 to the result list.
  - Update carry as the result divided by 2 (integer division).
  - Move both pointers to the left.
- After finishing, reverse the result list and join it into a final string.

## 📊 Complexity

- **Time Complexity:** $O(max(N, M))$  
Where $N$ is the length of the first input string and $M$ is of the second one accordingly.


- **Space Complexity:** $O(N + M)$  
Where $N$ is the length of the first input string and $M$ is of the second one accordingly, to store them.

---

## 🧩 Code

```python3 []
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        extra_dec_place = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or extra_dec_place != 0:
            r = extra_dec_place
            if i >= 0:
                r += int(a[i])
                i -= 1
            if j >= 0:
                r += int(b[j])
                j -=1
            result.append(str(r % 2))
            extra_dec_place = r // 2
        return "".join(result)[::-1]
```

