# Solution for Zigzag Conversion
from typing import List


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


# Naive solution - recreate zigzag exactly as it is
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         columns = []
#         connection_columns_n = numRows - 2
#         i = 0
#         mode_full_column = True
#         while i < len(s):
#             if mode_full_column:
#                 column = s[i:i+numRows]
#                 if len(column) != numRows:
#                     column += " " * (numRows - len(column))
#                 columns.append(column)
#                 i += numRows
#                 mode_full_column = False
#             else:
#                 j = 1
#                 while i < len(s) and j <= connection_columns_n:
#                     column = [" "] * numRows
#                     column[numRows - 1 - j] = s[i]
#                     columns.append("".join(column))
#                     i += 1
#                     j += 1
#                 mode_full_column = True
#
#         result = []
#         for column_i in range(numRows):
#             for column in columns:
#                 if column[column_i] != " ":
#                     result.append(column[column_i])
#         result = "".join(result)
#         return result
