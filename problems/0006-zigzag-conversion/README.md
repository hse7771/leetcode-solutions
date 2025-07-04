
# 🧠 Zigzag Conversion

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/zigzag-conversion/description/)

---

## 📝 Intuition

Simulate writing characters in a zigzag pattern by tracking rows dynamically instead of building a full grid. 
This avoids unnecessary space and simplifies the reconstruction process.

## 🔍 Approach

- Initialize an array of empty lists for each row.
- Use a pointer `cur_row` to track the current row and a flag `going_down` to track direction.
- Iterate through each character in the string:
  - Append it to the current row.
  - Change direction if the top or bottom row is reached.
  - Move to the next row based on the current direction.
- Finally, join all rows to form the resulting string.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input string, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows: List[List[str]] = [[] for _ in range(numRows)]
        cur_row = 0
        going_down = True
        for char in s:
            rows[cur_row].append(char)
            if going_down:
                cur_row += 1
            else:
                cur_row -= 1
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down

        return ''.join(''.join(row) for row in rows)
```

