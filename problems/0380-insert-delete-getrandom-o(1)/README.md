
# 🧠 Insert Delete Getrandom O(1)

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)

---

## 📝 Intuition

We need all three operations in (amortized) **O(1)**:
- A **hash map** gives O(1) insert/lookup/delete by value, but can’t pick a random element uniformly.
- An **array** lets us pick a **uniform random** element in O(1) by index, but deletions in the middle aren’t O(1).

Combine them:
- Keep values in an array `arr`.
- Keep a map `pos: value -> index in arr`.
- To delete in O(1), **swap** the element to remove with the last element, update that last element’s index in `pos`, then `pop()`.


## 🔍 Approach

- **insert(val)**: if `val` absent, append to `arr` and record its index in `pos[val]`.  
- **remove(val)**: if present at index `i_remove`, take `last_el = arr[-1]`, write it into `arr[i_remove]`, update `pos[last_el] = i_remove`, then `pop()` the tail and delete `pos[val]`.  
- **getRandom()**: return `arr[random.randrange(len(arr))]` — uniform over indices.

**Correctness sketch:**  
- `pos` always mirrors positions in `arr`.  
- Insert places `val` exactly once with its index recorded.  
- Remove keeps `arr` compact by swap-and-pop and fixes the moved element’s index, so future lookups remain valid.  
- Random is uniform because it samples a uniform index from `0..len(arr)-1`.

## 📊 Complexity

- **Time Complexity:** $O(1)$  
All three operations are $O(1)\space average$ (hash map + tail `pop()`; `getRandom` is O(1) index pick).


- **Space Complexity:** $O(N)$  
$N$ is the number of elements to store.

---

## 🧩 Code

```python3 []
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
```

