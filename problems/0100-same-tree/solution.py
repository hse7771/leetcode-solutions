# Solution for Same Tree
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


# DFS approach
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#
#         def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#             if root1 and root2:
#                 if root1.val != root2.val:
#                     return False
#                 return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
#             elif not root1 and not root2:
#                 return True
#             return False
#
#         return dfs(p, q)
