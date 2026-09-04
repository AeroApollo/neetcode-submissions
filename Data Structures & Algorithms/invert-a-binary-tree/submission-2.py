# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # brute force traverse the whole tree with BFS to get full count
        # idaelly we track the numbers involved per level
        # full count per level
        # we switch the numbers based on the list of numbers available at that level

        #queue: add number left to right: ideally full queue 2....7
        # use list but could be issue O(n) ez switch to queue
        curr = root
        q = deque()
        #print(q.pop()) #IndexError: pop from an empty deque
        while curr:
            print(curr.val)
            # skip nodes that have children
            # what if 1 node
            # right goes to left and left goes to right
            if not curr.left and not curr.right:
                if not q:
                    break
                curr = q.popleft()
                continue
            elif curr.left and not curr.right:
                #print('blah')
                curr.right = curr.left
                curr.left = None
            elif curr.right and not curr.left:
                curr.left = curr.right
                curr.right = None
            else:
                # level by level
                tmp = curr.right
                curr.right = curr.left
                curr.left = tmp

            q.append(curr.right)
            q.append(curr.left)
            #print(curr.right.val)
            #print(q)
            #print('lala',q.pop()) #this point to memory add 3
            
            # we need toacount for the popleft being a null otherwise it stops
            while q[0] is None:
                q.popleft()
            curr = q.popleft() #
            #print(curr.val)
        return root





