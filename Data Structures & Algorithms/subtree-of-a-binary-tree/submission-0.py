# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we only start subtree alg when the root.val == subRoot.val
        #base case
        if not root: return False #if root doesn't exist then return false
        elif self.exact_match(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def exact_match(self, p,q):
        if not p and not q: return True
        elif (p and not q) or (not p and q) or p.val != q.val:
            return False
        return self.exact_match(p.left,q.left) and self.exact_match(p.right,q.right)
