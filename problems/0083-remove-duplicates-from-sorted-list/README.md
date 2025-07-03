
# 🧠 Remove Duplicates From Sorted List

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

---

## 📝 Intuition

Perform basic linked list traversal.

## 🔍 Approach

1. Initialize a pointer `cur` to the head.
2. Traverse the list:
   - If `cur` and `cur.next` have equal values, skip the next node by updating `cur.next`.
   - Otherwise, move `cur` to the next node.
3. Return the head of the modified list.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
```

