# Solution for Pascal'S Triangle
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(2, numRows + 1):
            row = [1] * i
            for j in range(1, i - 1):
                row[j] = rows[i - 2][j - 1] + rows[i - 2][j]
            rows.append(row)
        return rows
