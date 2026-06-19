class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visisted_set=set()
        counter=0
        directions=[(0,-1),(-1,0),(1,0),(0,1)]
        def bfs(grid,row,col,visisted_set):
            queue=collections.deque()
            queue.append((row,col))
            visisted_set.add((row,col))
            while queue:
                r,c=queue.popleft()
                visisted_set.add((r,c))
                for dr,dc in directions:
                    new_row=r+dr
                    new_col=c+dc
                    if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and  grid[new_row][new_col]=='1' and (new_row,new_col) not in visisted_set:
                        queue.append((new_row,new_col))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in visisted_set:
                    bfs(grid,i,j,visisted_set)
                    counter=counter+1
        return counter


        