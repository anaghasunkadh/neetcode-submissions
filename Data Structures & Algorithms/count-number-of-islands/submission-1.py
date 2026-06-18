class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_set = set()
        counter=0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(i,j,visited_set,grid):
            queue = collections.deque()
            queue.append((i,j))
            while queue:
                row,col=queue.popleft()
                visited_set.add((row,col))
                for dr,dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if  new_row>=0 and new_row<len(grid) and new_col>=0 and new_col< len(grid[0]) and grid[new_row][new_col] =='1' and  (new_row,new_col) not in visited_set:
                        queue.append((new_row,new_col))
                        visited_set.add((new_row,new_col))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited_set and grid[i][j]=='1':
                    bfs(i,j,visited_set,grid)
                    counter = counter+1
        return counter