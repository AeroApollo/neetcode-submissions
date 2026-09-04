# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        elif not root.left and not root.right: return 1
        elif root.left and not root.right:
            return 1 + self.maxDepth(root.left)
        elif not root.left and root.right:
            return 1 + self.maxDepth(root.right)
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if left > right: return 1+left
            else: return 1+right