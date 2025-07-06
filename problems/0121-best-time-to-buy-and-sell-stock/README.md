
# 🧠 Best Time To Buy And Sell Stock

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

---

## 📝 Intuition

Use 2 pointers idea.

## 🔍 Approach

- Initialize a pointer `left` at the start of the array, representing the best day to buy so far.
- Iterate through the array with a `right` pointer (from index 1 onward), representing the current selling day.
- For each day:
  - Calculate the profit by subtracting the minimum buy price (`prices[left]`) from the current price (`prices[right]`).
  - If this profit is higher than the current maximum, update the maximum profit.
  - If a new minimum price is found at `prices[right]`, move the `left` pointer to `right` (since buying at a lower price is always better).
- At the end, return the highest profit found.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of elements in the input array.


- **Space Complexity:** $O(1)$  
No extra memory needed.

---

## 🧩 Code

```python3 []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(1, len(prices)):
            profit = max(profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
        return profit
```

