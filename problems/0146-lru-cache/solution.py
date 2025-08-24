# Solution for Lru Cache

class ListNode:
    def __init__(self, key=0, val=0, prev=None, next_p=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next_p


class LRUCache:
    def __init__(self, capacity: int):
        self.hash_table = {}
        self.capacity = capacity

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_after_head(self, node: ListNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: ListNode) -> None:
        prev, next_p = node.prev, node.next
        prev.next = next_p
        next_p.prev = prev

    def _move_to_front(self, node: ListNode) -> None:
        self._remove_node(node)
        self._add_after_head(node)

    def _pop_lru(self) -> ListNode:
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node

    def get(self, key: int) -> int:
        node = self.hash_table.get(key)
        if not node:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.hash_table.get(key)
        if node:
            node.val = value
            self._move_to_front(node)
        else:
            new_node = ListNode(key, value)
            self.hash_table[key] = new_node
            self._add_after_head(new_node)

            if len(self.hash_table) > self.capacity:
                node = self._pop_lru()
                self.hash_table.pop(node.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
