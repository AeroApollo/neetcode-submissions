"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we need to create an adjancency list

        #let's use a while loop to iterate through the nodes and store the neighbors in a list
        # we enter the while loop
            # curr has a val and neighbors which is actually a list of nodes
            # i mean the simple solution seems like for every node curr we do a for loop through the neighbors CANNOT append the list neighbors to output because we need a list to ints not memory addys
            # the issue with this is how to control the order
            # simple way to order this is a dictionary first and then go through dictionary to make a list
        '''
        output = []
        nodes_dict = {}
        visited = set()

        #print(node.neighbors)
        
        # BFS approach
        q = [node]
        while q:
            curr = q.pop(0)
            #print('blah',curr)
            #print(curr.val)
            if curr.val not in visited:
                visited.add(curr.val)
                #nodes_dict[curr.val] = set()
                new_node = Node(curr.val) #create new node without neighbors
                for i in range(len(curr.neighbors)):
                    nodes_dict[curr.val].add(curr.neighbors[i].val)
                    q.append(curr.neighbors[i])
                #print(q)
        #print(nodes_dict)
        '''
        old2new = {}

        def dfs(node):
            if node in old2new: #if node copy is already created    
                return old2new[node] #return the copy
            copy = Node(node.val) #create copy
            old2new[node] = copy #add hash to dict
            # now we need to traverse the neigbors
            for i in node.neighbors: #for the neighbors
                copy.neighbors.append(dfs(i)) #append i neighbor to copy
            return copy
        return dfs(node) if node else None
        