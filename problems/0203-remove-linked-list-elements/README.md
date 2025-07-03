
# 🧠 Remove Linked List Elements

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/description/)

---

## 📝 Intuition

Perform basic linked list traversal.

## 🔍 Approach

1. Initialize a pointer `cur` to the head.
2. Traverse the list starting from the head:
   - If `cur.next.val` equals the target value, skip `cur.next`.
   - Otherwise, move `cur` to `cur.next`.
3. Check if the head node itself needs to be removed and update it accordingly.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if head.val == val:
            head = head.next
        return head
```

