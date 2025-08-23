# Solution for Insert Delete Getrandom O(1)
import random


class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.pos[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        i_remove = self.pos[val]
        last_el = self.arr[-1]
        self.pos[last_el] = i_remove
        self.arr[i_remove] = last_el

        self.arr.pop()
        self.pos.pop(val)
        return True

    def getRandom(self) -> int:
        return self.arr[random.randrange(len(self.arr))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
