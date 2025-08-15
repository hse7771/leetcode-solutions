
# 🧠 Jewels And Stones

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/jewels-and-stones/description/)

---

## 📝 Intuition

Hash array to optimize search operation and perform basic array traversal.

## 🔍 Approach

1. Convert the string `jewels` into a hash set for $O(1)$ membership checks.
2. Initialize a counter to zero.
3. Iterate through each character in `stones`:
   - If the character is in the `jewels` set, increment the counter.
4. Return the counter as the total number of stones that are jewels.

## 📊 Complexity

- **Time Complexity:** $O(N + M)$  
$N$ and $M$ are the number of elements in the input strings.


- **Space Complexity:** $O(N + M)$  
$N$ and $M$ are the number of elements in the input strings, to store them. Also storing hash table.

---

## 🧩 Code

```python3 []
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_table = set(jewels)
        count = 0
        for stone in stones:
            if stone in hash_table:
                count += 1
        return count
```

