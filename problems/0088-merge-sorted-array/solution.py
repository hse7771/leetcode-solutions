# Solution for Merge Sorted Array
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        k = n + m - 1
        while i != -1 and j != -1:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # if elements in nums1 left (i) - they are already in place
        while j != -1:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
