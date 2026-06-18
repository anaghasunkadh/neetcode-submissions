class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        visisted_set = set()
        counter=0
        queue = collections.deque()
        def bfs(visisted_set,grid,row,col):
            queue.append((row,col))
            while queue:
                row,col = queue.popleft()
                visisted_set.add((row,col))
                for dr,dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if new_row>=0 and new_row<len(grid) and new_col>=0 and new_col<len(grid[0]) and grid[new_row][new_col]=="1" and (new_row,new_col) not in visisted_set:
                        queue.append((new_row,new_col))
                        visisted_set.add((new_row,new_col))

    
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visisted_set:
                    bfs(visisted_set,grid,i,j)
                    counter=counter+1
        return counter


                
        
        