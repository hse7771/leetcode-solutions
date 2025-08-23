# Solution for Maximal Square
from typing import List


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
