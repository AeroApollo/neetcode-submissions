# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we pass true if the val, left, and right are the same for p and q
        # otherwise false
        #print(p.val,q.val,p.val==q.val)
        #print(p.left==q.left)
        #print(p.val!=q.val,p.left.val!=q.left.val,p.right.val!=q.right.val)
        if (p and not q) or (not p and q): return False
        # we established that p and q must either both exist or both be null
        elif not p and not q: return True #if both null
        # then both exist so check children

        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    #1 = 1 2=2 3=3 