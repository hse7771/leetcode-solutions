
# 🧠 Merge Two Sorted Lists

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/description/)

---

## 📝 Intuition

Basic linked list traversal algorithm.

## 🔍 Approach

1. Initialize a dummy head node to simplify edge cases and a `cur` pointer for building the result.
2. Traverse both input linked lists:
   - At each step, compare the current values.
   - Append the smaller node to the result, and advance that list’s pointer.
3. After one list is exhausted, append the remainder of the other list.
4. Return the merged list (skipping the dummy head).

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the total number of nodes in both input lists.


- **Space Complexity:** $O(N)$  
$N$ is the total length of 2 input linked lists to store them.

---

## 🧩 Code

```python3 []
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        head = ListNode()
        cur = head
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2
        return head.next
```