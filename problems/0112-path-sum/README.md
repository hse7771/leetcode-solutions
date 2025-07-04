
# 🧠 Path Sum

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/path-sum/description/)

---

## 📝 Intuition

Perform basic tree traversal.

## 🔍 Approach

- Use DFS to traverse each root-to-leaf path.
- At each node, accumulate the running sum.
- If a leaf node is reached, check if the accumulated sum equals `targetSum`.
- Return `True` if any path matches; otherwise, continue searching.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the input tree.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the input tree, to store it.

---

## 🧩 Code

```python3 []
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root: Optional[TreeNode], targetSum: int, s: int = 0) -> bool:
            if not root:
                return False
            s += root.val
            if root.left is None and root.right is None:
                return s == targetSum
            return dfs(root.left, targetSum, s) or dfs(root.right, targetSum, s)

        return dfs(root, targetSum)
```

