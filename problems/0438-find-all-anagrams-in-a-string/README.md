
# 🧠 Find All Anagrams In A String

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)

---

## 📝 Intuition
Use hash tables as frequency counters and sliding window to optimize recounting of frequency.

## 🔍 Approach
1. Use a hash table to store the frequency of each character in `p` (`pattern_count`).
2. Initialize a sliding window of length equal to `p` in `s` and count the frequency of relevant characters (`window_count`).
3. Use a difference counter (`diff`) to keep track of mismatches between the current window and the target pattern.
4. For each new character entering the window and each character leaving the window:
   - Adjust `window_count` accordingly.
   - Update `diff` to reflect the change in matching status for that character.
5. If `diff` is zero after window update, it means the current window is an anagram of `p`, so record the starting index.
6. Repeat this process until the end of `s` and return all starting indices of found anagrams.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string $s$.


- **Space Complexity:** $O(K)$  
$K$ is the length of the input string $p$, to store hash tables. 

---

## 🧩 Code

```python3 []
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
```

