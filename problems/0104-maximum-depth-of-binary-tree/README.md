
# 🧠 Maximum Depth Of Binary Tree

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

---

## 📝 Intuition

Perform dfs or bfs algorithm to count the depth of the tree.

## 🔍 Approach

- Use a recursive DFS function:
  - If the current node is `None`, return 0.
  - Otherwise, return `1 + max(depth of left subtree, depth of right subtree)`.
- The final returned value is the maximum depth of the tree.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the input tree.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the input tree, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode]) -> int:
            if root:
                return 1 + max(dfs(root.left), dfs(root.right))
            return 0

        return dfs(root)
```

