from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # empty tree is balanced

        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))

        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)

        print(left_depth, right_depth)

        return abs(left_depth - right_depth) <= 1