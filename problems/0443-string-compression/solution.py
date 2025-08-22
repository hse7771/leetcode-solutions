# Solution for String Compression
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        def insert_group_length(start_i, length, array):
            string_number = list(str(length))
            for char in string_number:
                array[start_i] = char
                start_i += 1
            return len(string_number)

        cur_length = 1
        insert_pointer = 1
        for i in range(1, len(chars)):
            if chars[i - 1] != chars[i]:
                if cur_length > 1:
                    step = insert_group_length(insert_pointer, cur_length, chars)
                    insert_pointer += step
                cur_length = 1
                chars[insert_pointer] = chars[i]
                insert_pointer += 1
            else:
                cur_length += 1
        if cur_length > 1:
            step = insert_group_length(insert_pointer, cur_length, chars)
            insert_pointer += step
        return insert_pointer
