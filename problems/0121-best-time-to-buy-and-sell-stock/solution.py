# Solution for Best Time To Buy And Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(1, len(prices)):
            profit = max(profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
        return profit
