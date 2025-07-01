# Solution for Valid Parentheses

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
