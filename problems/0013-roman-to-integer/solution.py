# Solution for Roman To Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_arabic = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        arabic = roman_to_arabic[s[0]]
        for i in range(1, len(s)):
            arabic += roman_to_arabic[s[i]]
            roman_digit = s[i - 1] + s[i]
            if roman_digit in roman_to_arabic:
                arabic -= (2 * roman_to_arabic[s[i - 1]])
        return arabic
