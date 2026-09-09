class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # need a nested for loop to go through every value in grid
        #let's say we implement a DFS for this
        # let's says we are a random node [i][j]
            # we need some indicator of hitting a new island like a boolean that is false until 1 is hit
            # which makes it True and goes through DFS. After DFS, it turns back to false
            # we should also try to save time by not activating DFS if that node has already been visited
            # so a grand set of visited which contain tuples (i,j)
                
            # ideally we would follow the trail of 1s vert or hor until we hit matrix edge or zero
                # so at a node
                    # if a node is unvisited, add that node to the set of that island
                        # we should have an incrementor
                    # if above exists, go to that rec(up)
                    # then if right exists go to that rec(right)
                    # then if down exists go to that rec(down)
                    # then if left exists go to that rec(left)
                    # base case is all ver and hor values are 0 then do nothing
                    
            # i would use a dictionary here where each island is a key and the value is a set of ones
            # by construction of an island, two islands will never be directly next to each other vert of horizontal
        # at the end we can get len dictionary to get the number of islands

        # technically we don't need to track the each island...
        # so don't need adictionary. you could get by with a single set
        def DFS(i,j):
            #print(i,j)
            if (i,j) not in visited and grid[i][j]=="1":
                #print(i,j)
                visited.add((i,j))
                if i - 1 >= 0: 
                    DFS(i-1,j)
                if i + 1 < m:
                    DFS(i+1,j)
                if j-1 >= 0:
                    DFS(i,j-1)
                if j+1 < n:
                    DFS(i,j+1)
                return
            else:
                return

        visited = set()
        num_island = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visited:
                    num_island += 1
                    #visited.add((i,j)) #add tuple in visited
                    #print(visited)
                    DFS(i,j) #prupose of DFS is to update visited with all the 1s to the island
                #print(visited,num_island)
        return num_island

                
        


        
