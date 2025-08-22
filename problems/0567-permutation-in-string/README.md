
# 🧠 Permutation In String

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/permutation-in-string/description/)

---

## 📝 Intuition

Use sliding window idea and hashing array/string for frequency approach.

## 🔍 Approach

1. If `len(s1) > len(s2)`, return `False` (window can’t fit).
2. Build a frequency map `base_word_frequency` for `s1`.
3. Build the frequency map `cur_sequence_frequency` for the first window of `s2` (size `len(s1)`).
4. If the two maps are equal, return `True`.
5. Slide the window one character at a time across `s2`:
   - Decrement the count for the outgoing character; remove it from the map if the count hits zero.
   - Increment the count for the incoming character.
   - If the maps are equal, return `True`.
6. If no window matches, return `False`.

This keeps comparisons cheap because the alphabet is small (lowercase letters), and removing zero-count keys avoids map bloat.

## 📊 Complexity

- **Time Complexity:** $O(M)$  
$M$ is the length of the second string.


- **Space Complexity:** $O(N + M)$  
$N$ and $M$ are lengths of the input strings and up to $O(N)$ elements to store in the hash table,
but as long as we have the constraint of 26 on alphabet length it becomes $O(1)$.

---

## 🧩 Code

```python3 []
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
```

