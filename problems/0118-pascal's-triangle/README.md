
# 🧠 Pascal'S Triangle

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/pascals-triangle/description/)

---

## 📝 Intuition

Find the pattern how to build the next row in the triangle based on the previous one.

## 🔍 Approach

- Start with the first row `[1]`.
- For each next row, initialize a list of ones with the required length.
- For each interior element, set its value to the sum of the two elements above it from the previous row.
- Append each constructed row to the result list.
- Continue this process until the required number of rows is generated.

## 📊 Complexity

- **Time Complexity:** $O(N^2)$  
$N$ is `numRows`. Each row has up to $N$ elements, and all rows are filled.


- **Space Complexity:** $O(N^2)$  
  All rows are stored in the output list.


---

## 🧩 Code

```python3 []
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(2, numRows + 1):
            row = [1] * i
            for j in range(1, i - 1):
                row[j] = rows[i - 2][j - 1] + rows[i - 2][j]
            rows.append(row)
        return rows
```

