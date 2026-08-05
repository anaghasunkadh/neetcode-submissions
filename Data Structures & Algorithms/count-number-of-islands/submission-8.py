class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visisted_set=set()
        queue=collections.deque()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        counter=0
        def bfs(i,j,visisted_set,queue,grid):
            queue.append((i,j))
            visisted_set.add((i,j))
            while queue:
                row,col=queue.popleft()
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[i]) and  (nr,nc) not in visisted_set and grid[nr][nc]=="1":
                        queue.append((nr,nc))
                        visisted_set.add((nr,nc))
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visisted_set and grid[i][j]=="1":
                    bfs(i,j,visisted_set,queue,grid)
                    counter=counter+1
        return counter
        