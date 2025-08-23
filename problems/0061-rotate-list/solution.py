# Solution for Rotate List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
