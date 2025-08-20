
# 🧠 Generate Parentheses

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/generate-parentheses/description/)

---

## 📝 Intuition

We want all strings of length `2n` with balanced parentheses.  
A valid partial string must satisfy two invariants at every step:
- The number of `'('` used is at most `n`.
- The number of `')'` used is at most the number of `'('` already placed.

Backtracking from the empty prefix and enforcing these invariants prunes all invalid branches early, 
leaving exactly the valid (Catalan) solutions.

## 🔍 Approach

Maintain two counters:  
- `open` — how many `'('` we have placed,  
- `close` — how many `')'` we have placed.

At each step:
- If `open < n`, we may place `'('`.  
- If `close < open`, we may place `')'`.  
Once the prefix length reaches `2n`, add it to the result.

This explores only feasible prefixes.

## 📊 Complexity

- **Time Complexity:** $Θ(C_n \cdot n)$  
  Where $C_n = \frac{1}{n+1}\binom{2n}{n}$ is the nth Catalan number; each output string has length `2n`.
<!-- e.g. $$O(n)$$ -->


- **Space Complexity:** $O(N)$  
Recursion depth / prefix buffer (excluding the output list).

---

## 🧩 Code

```python3 []
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generate_combinations(prefix: List[str], count: dict[str, int]) -> None:
            if len(prefix) == n * 2:
                result.append("".join(prefix))
                return
            for symb in alphabet:
                count[symb] += 1
                if count["("] > n:
                    count["("] -= 1
                    continue
                elif count[")"] > count["("]:
                    count[")"] -= 1
                    continue
                prefix.append(symb)
                generate_combinations(prefix, count)
                prefix.pop(-1)
                count[symb] -= 1

        result = []
        alphabet = "()"
        generate_combinations([], {"(": 0, ")": 0})
        return result
```

