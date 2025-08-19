
# 🧠 Reverse Linked List

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/reverse-linked-list/description/)

---

## 📝 Intuition

Perform basic linked list traversal and redirect nodes pointers.

## 🔍 Approach

1. Initialize `prev = None` and `curr = head`.  
2. While `curr` is not `None`:  
   - Save `curr.next` in a temporary variable.  
   - Redirect `curr.next` to `prev`.  
   - Move `prev` forward to `curr`.  
   - Move `curr` forward to the saved `next`.  
3. At the end, `prev` points to the new head of the reversed list.  
4. Return `prev`.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
```

