
# 🧠 Intersection Of Two Arrays Ii

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)

---

## 📝 Intuition

Hash input array for optimizing search operations and perform basic array traversal.

## 🔍 Approach

1. Ensure `nums1` is the longer array to minimize hash table size.
2. Build a frequency map (`hash_table`) for the shorter array:
   - Keys are elements
   - Values are counts of occurrences
3. Initialize an empty result list.
4. Traverse the longer array:
   - If the element is in the hash table with a positive count:
     - Append it to the result
     - Decrement its count in the hash table
5. Return the result list containing all intersections.

## 📊 Complexity

- **Time Complexity:** $O(N + M)$  
$N$ and $M$ are the lengths of the input arrays.


- **Space Complexity:** $O(N + M)$  
$N$ and $M$ are the lengths of the input arrays and up to $min(N, M)$ elements to store in hash table. 

---

## 🧩 Code

```python3 []
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
```

