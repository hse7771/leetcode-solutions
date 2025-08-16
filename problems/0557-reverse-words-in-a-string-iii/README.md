
# 🧠 Reverse Words In A String Iii

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-iii/description/)

---

## 📝 Intuition

Perform basic string traversal and reverse each string part (single word).

## 🔍 Approach

1. Split the string `s` by spaces into a list of words.
2. For each word in the list:
   - Reverse it using slicing `[::-1]`.
3. Join the reversed words back into a single string separated by spaces.
4. Return the resulting string.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input string, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)
```

