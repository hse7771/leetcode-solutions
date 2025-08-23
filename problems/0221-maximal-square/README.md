
# 🧠 Maximal Square

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/maximal-square/description/)

---

## 📝 Intuition

Use dynamic programming and understand the mechanism of getting larger square from already existing ones (main formula).

## 🔍 Approach

1. Treat the first row as the base DP row: convert `"0"/"1"` to integers; initialize the current **max side** with the max of that row.
2. For each subsequent row:
   - Build a `cur_row` DP array of length `n` (initialized with zeros).
   - For each column `j`:
     - If `matrix[i][j] == "1"`:
       - If `j == 0`, set `cur_row[j] = 1` (no left/top-left neighbors).
       - Else set `cur_row[j] = min(prev_row[j - 1], prev_row[j], cur_row[j - 1]) + 1`.
     - Update the running maximum side length.
   - Set `prev_row = cur_row` and continue.
3. Return `mx * mx` (area from the maximal side).

This uses only the **previous DP row** plus the current row → space-optimized DP.

## 📊 Complexity

- **Time Complexity:** $O(N\cdot M)$  
$N$ and $M$ are sizes of the matrix.


- **Space Complexity:** $O(N\cdot M)$   
Up to $O(N)$ for dp calculations as only one row is stored at a time.

---

## 🧩 Code

```python3 []
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prev_row = list(map(int, matrix[0].copy()))
        mx = max(prev_row)
        for i in range(1, m):
            cur_row = [0 for _ in range(n)]
            for j in range(n):
                if matrix[i][j] == "1":
                    if j > 0:
                        cur_row[j] = min(prev_row[j - 1], prev_row[j], cur_row[j - 1]) + 1
                    else:
                        cur_row[j] = 1
                mx = max(mx, cur_row[j])
            prev_row = cur_row
        return mx * mx
```

