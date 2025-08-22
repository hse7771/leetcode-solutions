# Solution for Summary Ranges
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 == end:
                end = nums[i]
            else:
                if start != end:
                    result.append(f"{start}->{end}")
                else:
                    result.append(str(start))
                start = end = nums[i]
        if start != end:
            result.append(f"{start}->{end}")
        else:
            result.append(str(start))
        return result
