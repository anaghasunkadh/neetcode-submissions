class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(sr,sc,color,image):
            if image[sr][sc] == color:return
            visited_set = set()
            queue = collections.deque()
            original_color=image[sr][sc]
            image[sr][sc] = color
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            queue.append((sr,sc))
            while queue:
                row,col = queue.popleft()
                visited_set.add((row,col))
                for dr,dc in directions:
                    new_row = row+dr
                    new_col = col+dc
                    if new_row >=0 and new_row < len(image) and new_col >=0 and new_col<len(image[0]) and image[new_row][new_col] == original_color:
                            queue.append((new_row,new_col))
                            visited_set.add((new_row,new_col))
                            image[new_row][new_col] = color
        bfs(sr,sc,color,image)
        return image
        