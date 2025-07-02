# Solution for Longest Common Prefix
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = min(strs, key=len)
        for i in range(len(lcp)):
            for s in strs:
                if s[i] != lcp[i]:
                    return lcp[:i]
        return lcp
