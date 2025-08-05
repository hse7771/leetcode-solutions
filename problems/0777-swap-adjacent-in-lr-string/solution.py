# Solution for Swap Adjacent In Lr String

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        i, j = 0, 0
        n = len(start)
        while i < n and j < n:
            if start[i] != "X" and result[j] != "X":
                if start[i] != result[j]:
                    return False
                elif start[i] == "L" and i < j:
                    return False
                elif start[i] == "R" and i > j:
                    return False
                i += 1
                j += 1
            while i < n and start[i] == "X":
                i += 1
            while j < n and result[j] == "X":
                j += 1
        return i == j
