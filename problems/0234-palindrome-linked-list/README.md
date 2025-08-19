
# 🧠 Palindrome Linked List

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/palindrome-linked-list/description/)

---

## 📝 Intuition

Use slow/fast pointers approach and then reverse the second half of the linked list.

## 🔍 Approach

1. Use **slow/fast pointers** to find the midpoint of the list.  
   - If the length is odd, move `slow` one extra step to skip the middle node.  
2. Reverse the second half of the list in place.  
3. Compare the first half and the reversed second half node by node.  
   - If all values match, it’s a palindrome.  
   - Otherwise, it’s not.  
4. (Optional) Restore the list to its original structure by reversing the second half back.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the input linked list, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        cur1, cur2 = head, prev
        while cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True
```

