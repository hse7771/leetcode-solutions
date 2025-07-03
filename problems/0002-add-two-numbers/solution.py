# Solution for Add Two Numbers
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
