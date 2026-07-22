class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visisted_set=set()
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        time=0
        counter=0
        queue=collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    queue.append((i,j,time))
                if grid[i][j]==1:
                    counter=counter+1
        while queue:
            row,col,time=queue.popleft()
            visisted_set.add((row,col))
            for dr,dc in directions:
                nrow=row+dr
                ncol=col+dc
                if 0<=nrow<len(grid) and 0<=ncol<len(grid[i]) and (nrow,ncol) not in visisted_set and grid[nrow][ncol]==1:
                    grid[nrow][ncol]=2
                    counter=counter-1
                    queue.append((nrow,ncol,time+1))
        if counter==0:
            return time
        else:
            return -1

                    


        