class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid,i,j,visited_set):
            queue = collections.deque()
            queue.append([i,j])
            visited_set.add((i,j))
            while queue:
                row,col = queue.popleft()
                visited_set.add((row,col))
                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                for dr,dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if (new_row,new_col) not in visited_set and 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col]== "1" :
                        queue.append([new_row,new_col])
                        visited_set.add((new_row,new_col))
        visited_set = set()
        counter= 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]== "1" and (i,j) not in visited_set:
                    bfs(grid,i,j,visited_set)
                    counter = counter+1
        return counter



        