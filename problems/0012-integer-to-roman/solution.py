# Solution for Integer To Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numbers = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman_translation = []
        for part in roman_numbers:
            while num >= part:
                num -= part
                roman_translation.append(roman_numbers[part])
        return "".join(roman_translation)
