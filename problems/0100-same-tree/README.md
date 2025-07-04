
# 🧠 Same Tree

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/same-tree/description/)

---

## 📝 Intuition

Implement either DFS or BFS algorithm and perform basic tree traversal.

## 🔍 Approach

1. Implement DFS or BFS algorithm.
2. Compare all node values in their order.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes visited. It is either $2 \cdot N$ or these are not equal trees and returned early.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the first input tree and $M$ is in the second one accordingly, to store them.

---

## 🧩 Code

```python3 []
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            queue = deque([root1, root2])
            while queue:
                for i in range(0, len(queue), 2):
                    node1, node2 = queue.popleft(), queue.popleft()
                    if not node1 and not node2:
                        continue
                    elif not node1 or not node2:
                        return False
                    if node1.val != node2.val:
                        return False
                    queue.append(node1.left)
                    queue.append(node2.left)
                    queue.append(node1.right)
                    queue.append(node2.right)
            return True

        return bfs(p, q)
```

