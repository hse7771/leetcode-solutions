# Solution for Permutation In String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        base_word_frequency = {}
        for letter in s1:
            base_word_frequency[letter] = base_word_frequency.get(letter, 0) + 1
        cur_sequence_frequency = {}
        for i in range(n1):
            cur_sequence_frequency[s2[i]] = cur_sequence_frequency.get(s2[i], 0) + 1
        if cur_sequence_frequency == base_word_frequency:
            return True
        for j in range(n1, n2):
            symb_out, symb_in = s2[j - n1], s2[j]
            cur_sequence_frequency[symb_out] -= 1
            if cur_sequence_frequency[symb_out] == 0:
                cur_sequence_frequency.pop(symb_out)
            cur_sequence_frequency[symb_in] = cur_sequence_frequency.get(symb_in, 0) + 1
            if cur_sequence_frequency == base_word_frequency:
                return True
        return False
