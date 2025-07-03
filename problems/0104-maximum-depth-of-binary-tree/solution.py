# Solution for Maximum Depth Of Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode]) -> int:
            if root:
                return 1 + max(dfs(root.left), dfs(root.right))
            return 0

        return dfs(root)

# BFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#
#         def bfs(root: Optional[TreeNode]) -> int:
#             depth = 0
#             if not root:
#                 return depth
#
#             queue = deque([root])
#             while queue:
#                 for _ in range(len(queue)):
#                     node = queue.popleft()
#                     if node.left:
#                         queue.append(node.left)
#                     if node.right:
#                         queue.append(node.right)
#                 depth += 1
#             return depth
#
#         return bfs(root)
