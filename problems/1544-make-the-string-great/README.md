
# 🧠 Make The String Great

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/make-the-string-great/description/)

---

## 📝 Intuition

Use stack data structure. Avoid deleting from middle of the array that causes shifting elements and inefficiency.

## 🔍 Approach

1. Initialize an empty stack.
2. For each character in the string:
    - If the stack is not empty and the top of the stack is the same letter (case-insensitive) but different case, pop from the stack (this pair "cancels out").
    - Otherwise, push the current character onto the stack.
3. Finally, join the stack into a string and return it.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the string to store it, stack cannot be more than that.

---

## 🧩 Code

```python3 []
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1].lower() == s[i].lower() and stack[-1] != s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
```

