# Solution for Range Sum Of Bst
from typing import Optional


# Definition for a binary tree node.
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

# BFS approach
# from collections import deque
# def bfs(root: Optional[TreeNode]) -> int:
#     queue = deque([root])
#     s = 0
#     while queue:
#         root = queue.popleft()
#         if not root:
#             continue
#         if root.val < low:
#             queue.append(root.right)
#         elif root.val > high:
#             queue.append(root.left)
#         else:
#             s += root.val
#             queue.append(root.left)
#             queue.append(root.right)
#     return s
