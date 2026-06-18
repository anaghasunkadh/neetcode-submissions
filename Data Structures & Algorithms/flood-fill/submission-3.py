class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=0
        col=0
        originalcolor=image[sr][sc]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visisted_set=set((sr,sc))
        queue=collections.deque([(sr,sc)])
        if originalcolor==color:
                    return image
        image[sr][sc]=color
        while queue:
            nr,nc=queue.popleft()
            visisted_set.add((nr,nc))
            for dr,dc in directions:
                new_row=nr+dr
                new_col=nc+dc
                if 0<=new_row<len(image) and 0<=new_col<len(image[0]) and image[new_row][new_col]==originalcolor:
                    image[new_row][new_col]=color
                    queue.append((new_row,new_col))
        return image
                    
                

        