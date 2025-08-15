# Solution for Jewels And Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_table = set(jewels)
        count = 0
        for stone in stones:
            if stone in hash_table:
                count += 1
        return count
