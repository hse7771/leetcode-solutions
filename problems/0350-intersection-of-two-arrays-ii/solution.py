# Solution for Intersection Of Two Arrays Ii
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        hash_table = {}
        for el in nums2:
            hash_table[el] = hash_table.get(el, 0) + 1

        result = []
        for el in nums1:
            if el in hash_table and hash_table[el] > 0:
                result.append(el)
                hash_table[el] -= 1
        return result
