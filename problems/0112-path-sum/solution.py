# Solution for Path Sum
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
