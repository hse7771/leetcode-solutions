# Solution for Sort List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            head0 = ListNode()
            cur1, cur2, cur = head1, head2, head0
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next

            cur1 = cur1 or cur2
            cur.next = cur1
            return head0.next

        def merge_sort(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            head2 = merge_sort(slow.next)
            slow.next = None
            head1 = merge_sort(head)
            return merge(head1, head2)

        return merge_sort(head)
