
# 🧠 Rotate List

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/rotate-list/description/)

---

## 📝 Intuition

Perform basic linked list traversal. Perform necessary connection and cut between nodes.

## 🔍 Approach

1. Edge case: if `head` is `None`, return `None`.
2. Traverse once to get the **length `n`** and the **tail**; connect `tail.next = head` to form a cycle.
3. Reduce rotations: `k %= n`.
4. Starting from `head`, move `n - k - 1` steps to land on the **new tail**.
5. The **new head** is `new_tail.next`. Break the cycle by setting `new_tail.next = None`.
6. Return `new_head`.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n = 1
        curr = head
        while curr.next:
            n += 1
            curr = curr.next
        curr.next = head
        k %= n
        curr = head
        for i in range(n - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        return new_head
```

