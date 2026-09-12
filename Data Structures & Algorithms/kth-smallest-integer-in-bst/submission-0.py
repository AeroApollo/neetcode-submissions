# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # i would approach this as DFS and return the node val somehow
        # the question is how to track that
        # i wish somehow we could find t
        #honestly the easiest to BFS all the values into a list and then sort and then return k
        values = []
        q = [root]

        while q:
            curr_node = q.pop(0)
            values.append(curr_node.val)
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        #print(sorted(values))
        return sorted(values)[k-1]

