class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        visited_set = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        counter = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==2:
                    queue.append((i,j))
        if not queue:
            for row in grid:
                if 1 in row:
                    return -1
                return 0
                
        while queue:
            for _ in range(len(queue)):
                row,col = queue.popleft()
                visited_set.add((row,col))

                for dr,dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if new_row>=0 and new_col>=0 and new_row<len(grid) and new_col<len(grid[0]) and  grid[new_row][new_col] ==1:
                        queue.append((new_row,new_col))
                        visited_set.add((new_row,new_col))
                        grid[new_row][new_col]=2
            counter = counter+1
        for row in grid:
            if 1 in row:
                return -1
        return counter


            

                
        