
# 🧠 Valid Parentheses

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/valid-parentheses/description/)

---

## 📝 Intuition

Use stack data structure.

## 🔍 Approach

1. Define a mapping from opening to closing brackets.
2. Iterate through each character in the string:
    - If it’s an opening bracket, push it onto the stack.
    - If it’s a closing bracket, check if it matches the top element of the stack. If not, return False.
3. After processing the string, the stack should be empty for a valid input.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input string.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input string to store it and stack cannot be more than that.

---

## 🧩 Code

```python3 []
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if stack and char == brackets[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        return True
```

