# Solution for Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hast_table = {}
        hashed_chars = set()
        for s_ch, t_ch in zip(s, t):
            if s_ch not in hast_table:
                if t_ch in hashed_chars:
                    return False
                hast_table[s_ch] = t_ch
                hashed_chars.add(t_ch)
            else:
                if hast_table[s_ch] != t_ch:
                    return False
        return True
