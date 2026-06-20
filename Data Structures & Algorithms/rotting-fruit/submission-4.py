class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visisted_set=set()
        t=0
        max_time=0
        queue=collections.deque()
        directions=[(0,-1),(-1,0),(0,1),(1,0)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i,j,t))
                    visisted_set.add((i,j))
        while queue:
            row,col,t=queue.popleft()
            for dr,dc in directions:
                nrow=row+dr
                ncol=col+dc
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1 and (nrow,ncol) not in visisted_set:
                    visisted_set.add((nrow,ncol))
                    queue.append((nrow,ncol,t+1))
            max_time=max(max_time,t)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (i,j) not in visisted_set:
                    return -1
        return max_time

                    


            
        