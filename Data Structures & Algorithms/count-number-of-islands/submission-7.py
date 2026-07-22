class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visisted_set=set()
        counter=0
        def bfs(row,col,visisted_set,grid):
            queue=collections.deque()
            queue.append((row,col))
            while queue:
                row,col=queue.popleft()
                visisted_set.add((row,col))
                for dr,dc in directions:
                    nrow=row+dr
                    ncol=col+dc
                    if 0<=nrow<len(grid) and 0<=ncol<len(grid[nrow]) and (nrow,ncol) not in visisted_set and grid[nrow][ncol]=="1":
                        queue.append((nrow,ncol))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visisted_set and grid[i][j]=="1":
                    bfs(i,j,visisted_set,grid)
                    counter=counter+1
        return counter

        