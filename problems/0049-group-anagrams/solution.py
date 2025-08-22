# Solution for Group Anagrams
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for s in strs:
            key = tuple(sorted(s))
            hash_table.setdefault(key, []).append(s)
        return list(hash_table.values())
