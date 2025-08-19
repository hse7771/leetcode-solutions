
# 🧠 Remove Nth Node From End Of List

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

---

## 📝 Intuition

Perform basic linked list traversal and apply fast pointer approach.

## 🔍 Approach

1. Create a dummy node pointing to the head (to simplify removal at the first position).  
2. Place two pointers (`fast`, `curr`) at the dummy.  
3. Advance `fast` by `n` steps.  
4. Move both pointers forward until `fast.next` is `None`.  
   - At this point, `curr.next` is the node to be removed.  
5. Skip the target node: `curr.next = curr.next.next`.  
6. Return `dummy.next` as the new head.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(-1, head)
        curr = fast = head
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            curr = curr.next
            fast = fast.next
        curr.next = curr.next.next
        return head.next
```

