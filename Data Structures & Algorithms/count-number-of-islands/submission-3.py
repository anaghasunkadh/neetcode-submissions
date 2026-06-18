class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        row=0
        col=0
        counter=0
        visisted_set=set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(row,col,grid,visisted_set):
            queue=collections.deque([(row,col)])
            visisted_set.add((row,col))
            while queue:
                nrow,ncol=queue.pop()
                visisted_set.add((nrow,ncol))
                for dr,dc in directions:
                    new_row=nrow+dr
                    new_col=ncol+dc
                    if 0<=new_row<n and 0<=new_col<m and (new_row,new_col) not in visisted_set and grid[new_row][new_col]!='0':
                        queue.append((new_row,new_col))
        for row in range(n):
            for col in range(m):
                if grid[row][col]=='1' and (row,col) not in visisted_set:
                    bfs(row,col,grid,visisted_set)
                    counter=counter+1
        return counter



                
        
        
        