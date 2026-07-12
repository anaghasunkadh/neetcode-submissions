class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=collections.deque()
        visisted_set=set()
        time=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        counter=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    queue.append((i,j,time))
                if grid[i][j]==1:
                    counter=counter+1
        while queue:
            row,col,time=queue.popleft()
            visisted_set.add((row,col))
            for r,c in directions:
                nrow=row+r
                ncol=col+c
                if 0<=nrow<len(grid) and 0<=ncol<len(grid[nrow]) and grid[nrow][ncol]==1 and (nrow,ncol) not in visisted_set:
                    grid[nrow][ncol]=2
                    counter=counter-1
                    queue.append((nrow,ncol,time+1))
        if counter>0:
            return -1
        if counter<=0:
            return time

        

        