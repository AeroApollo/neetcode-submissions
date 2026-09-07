# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def valid(root,lBound,rBound):
            if lBound < root.val and root.val < rBound:
                if root.left and root.right: 
                    return valid(root.left,lBound,root.val) and valid(root.right,root.val,rBound)
                elif root.left: return valid(root.left,lBound,root.val)
                elif root.right: return valid(root.right,root.val,rBound)
                else: return True
            return False

        return valid(root,-float('Inf'),float('Inf'))

        # valid(root (2),-I,I)
        # -I < 2 and 2 < I and root.left so valid(root.left (1), -I, 2)
        # -I < 1 and 1 < 2 and not children (else) return True
            
        
