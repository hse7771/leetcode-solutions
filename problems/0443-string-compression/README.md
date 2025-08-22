
# 🧠 String Compression

> **Difficulty:** 🟡 **Medium**\
> 📎 [View on LeetCode](https://leetcode.com/problems/string-compression/description/)

---

## 📝 Intuition

Perform basic array traversal and use idea of insert pointers.

## 🔍 Approach

1. Maintain:
   - `insert_pointer` — where to write next,
   - `cur_length` — length of the current run.
2. Scan the array from left to right. Whenever the current character differs from the previous one, the **run ends**:
   - If `cur_length > 1`, write its length digits starting at `insert_pointer`, and advance the pointer.
   - Start the next run by writing its first character at `insert_pointer`, then advance the pointer.
3. After the loop, **flush** the final run’s length if needed.
4. Return `insert_pointer` (the new length).

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the length of the input array.


- **Space Complexity:** $O(N)$  
$N$ is the length of the input array, to store it.

---

## 🧩 Code

```python3 []
    def compress(self, chars: List[str]) -> int:

        def insert_group_length(start_i, length, array):
            string_number = list(str(length))
            for char in string_number:
                array[start_i] = char
                start_i += 1
            return len(string_number)

        cur_length = 1
        insert_pointer = 1
        for i in range(1, len(chars)):
            if chars[i - 1] != chars[i]:
                if cur_length > 1:
                    step = insert_group_length(insert_pointer, cur_length, chars)
                    insert_pointer += step
                cur_length = 1
                chars[insert_pointer] = chars[i]
                insert_pointer += 1
            else:
                cur_length += 1
        if cur_length > 1:
            step = insert_group_length(insert_pointer, cur_length, chars)
            insert_pointer += step
        return insert_pointer
```

