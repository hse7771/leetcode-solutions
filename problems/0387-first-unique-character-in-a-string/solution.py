# Solution for First Unique Character In A String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}
        for i in range(len(s)):
            if s[i] not in hash_table:
                hash_table[s[i]] = i
            else:
                hash_table[s[i]] = -1
        answer = -1
        for ch, idx in hash_table.items():
            if idx != -1:
                answer = idx
                break
        return answer

# Any lang stable approach:
# Count frequency and then just iterate initial string and return the first char with value 1
# Also an array can be used instead of hash table, array of size 26, as we have the constraint on input symbols
