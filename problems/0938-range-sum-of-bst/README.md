
# 🧠 Range Sum Of Bst

> **Difficulty:** 🟢 **Easy**\
> 📎 [View on LeetCode](https://leetcode.com/problems/range-sum-of-bst/description/)

---

## 📝 Intuition

Perform basic dfs or bfs tree traversal.

## 🔍 Approach

**DFS Recursive:**
1. Start at the root.
2. If the node is `None`, return `0`.
3. If `node.val < low`, skip the left subtree and recurse right.
4. If `node.val > high`, skip the right subtree and recurse left.
5. Otherwise, add `node.val` and recurse both left and right.
6. Return the accumulated sum.

## 📊 Complexity

- **Time Complexity:** $O(N)$  
$N$ is the number of nodes in the tree.


- **Space Complexity:** $O(N)$  
$N$ is the number of nodes in the tree, to store it.  
Also $O(H)$ for recursion stack, where $H$ is the tree height
and in the worst case $H = N$ (skewed tree).

---

## 🧩 Code

```python3 []
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            if root.val < low:
                return dfs(root.right)
            if root.val > high:
                return dfs(root.left)
            return root.val + dfs(root.left) + dfs(root.right)

        return dfs(root)
```

