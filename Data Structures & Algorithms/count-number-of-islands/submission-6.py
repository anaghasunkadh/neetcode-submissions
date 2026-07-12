class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        visisted_set=set()
        counter=0
        def bfs(ro,co,grid,visisted_set):
            queue=collections.deque()
            queue.append((ro,co))
            while queue:
                row,col=queue.popleft()
                visisted_set.add((row,col))
                for r,c in directions:
                    nrow=row+r
                    ncol=col+c
                    if (nrow,ncol) not in visisted_set and 0<=nrow<len(grid) and 0<=ncol<len(grid[nrow]) and grid[nrow][ncol]=="1":
                        queue.append((nrow,ncol))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visisted_set and grid[i][j]=="1":
                    bfs(i,j,grid,visisted_set)
                    counter=counter+1
        return counter

        