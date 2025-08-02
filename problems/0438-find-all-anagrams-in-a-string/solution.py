# Solution for Find All Anagrams In A String
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if n < k:
            return []

        pattern_count = {}
        for ch in p:
            pattern_count[ch] = pattern_count.get(ch, 0) + 1
        window_count = {}
        for i in range(k):
            if s[i] in pattern_count:
                window_count[s[i]] = window_count.get(s[i], 0) + 1
        diff = 0
        for key in pattern_count:
            if key in window_count:
                diff += int(not (window_count[key] == pattern_count[key]))
            else:
                diff += 1
        starts = [0] if diff == 0 else []

        for j in range(k, n):
            char_in, char_out = s[j], s[j - k]
            if char_out in pattern_count:
                if pattern_count[char_out] == window_count[char_out]:
                    diff += 1
                elif pattern_count[char_out] == window_count[char_out] - 1:
                    diff -= 1
                window_count[char_out] -= 1

            if char_in in pattern_count:
                window_count[char_in] = window_count.get(char_in, 0) + 1
                if pattern_count[char_in] == window_count[char_in] - 1:
                    diff += 1
                elif pattern_count[char_in] == window_count[char_in]:
                    diff -= 1

            if diff == 0:
                starts.append(j - k + 1)
        return starts
