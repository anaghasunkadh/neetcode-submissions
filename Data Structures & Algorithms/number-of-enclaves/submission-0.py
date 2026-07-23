class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visisted_set=set()
        queue=collections.deque()
        counter=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i==0 or i==len(grid)-1 or j==0 or j==len(grid[i])-1) and grid[i][j]==1:
                    queue.append((i,j))
                    visisted_set.add((i,j))
        while queue:
            row,col=queue.popleft()
            for dr,dc in directions:
                nrow=row+dr
                ncol=col+dc
                if 0<=nrow<len(grid) and 0<=ncol<len(grid[i]) and grid[nrow][ncol]==1 and (nrow,ncol) not in visisted_set:
                    queue.append((nrow,ncol))
                    visisted_set.add((nrow,ncol))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visisted_set and grid[i][j]==1:
                    counter=counter+1
        return counter 
        