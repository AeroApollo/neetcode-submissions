# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #print(root.val)
        if q.val<p.val:
            tmp = q
            q = p
            p = tmp
        if not root: return None
        #print(root.val >= p.val,root.val <= q.val) #5 >= 3 true 5 <= 4 false
        #print(p.val <= root.left.val,q.val <= root.left.val, q.val, root.left.val) #3 4 <= 5 True True
        #print(p.val >= root.right.val,q.val >= root.right.val) #3 4 >= 5: F F
        if root.val >= p.val and root.val <= q.val: return root
        elif p.val <= root.val and q.val <= root.val:
            #print('left')
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val >= root.val and q.val >= root.val:
            #print('right')
            return self.lowestCommonAncestor(root.right,p,q)