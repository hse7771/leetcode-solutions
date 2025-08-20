# Solution for Generate Parentheses
from typing import List


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
