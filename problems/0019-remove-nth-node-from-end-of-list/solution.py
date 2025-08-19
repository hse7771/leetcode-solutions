# Solution for Remove Nth Node From End Of List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
