
# 🧠 Add Two Numbers

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/add-two-numbers/description/)

---

## 📝 Intuition

Perform basic linked list traversal.

## 🔍 Approach

- Initialize a dummy head and a current pointer for the result linked list.
- Set `carry` to 0.
- Iterate while either linked list has nodes or there is a non-zero carry:
  - Sum values from current nodes of both lists (if they exist) plus carry.
  - Update carry for the next iteration.
  - Create a new node with the digit value and attach it to the result.
  - Advance input list pointers and the result pointer.

## 📊 Complexity

- **Time Complexity:** $O(max(N, M))$  
$N$ is number of nodes in the first input linked list and $M$ is in the second one respectively.


- **Space Complexity:** $O(N + M)$  
$N$ is number of nodes in the first input linked list and $M$ is in the second one respectively, to store them.

---

## 🧩 Code

```python3 []
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        additional_dec_place = 0
        result = ListNode()
        cur = result
        while cur1 or cur2 or additional_dec_place:
            val = additional_dec_place
            if cur1:
                val += cur1.val
                cur1 = cur1.next
            if cur2:
                val += cur2.val
                cur2 = cur2.next
                
            additional_dec_place = val // 10
            val %= 10
            cur.next = ListNode(val)
            cur = cur.next
            
        return result.next
```

