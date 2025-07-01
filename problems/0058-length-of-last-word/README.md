
# 🧠 Length Of Last Word

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/length-of-last-word/description/)

---

## 📝 Intuition

Basic traversal or remember python built-in methods.

## 🔍 Approach

- Iterate over each character in the string.
- If the character is not a space, increment the current word length.
- If a space is found, update the last word length if the current length is not zero, and reset the current count.
- At the end, check if the last word may have finished at the end of the string.

## 📊 Complexity

- **Time Complexity:**  $O(N)$  

$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  

$N$ is the length of the input string, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n_last = 0
        cur = 0
        for char in s:
            if char.isalpha():
                cur += 1
            else:
                if cur != 0:
                    n_last = cur
                cur = 0
        if cur != 0:
            n_last = cur
        return n_last
```

