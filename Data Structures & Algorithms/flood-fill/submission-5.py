class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalcolor=image[sr][sc]
        directions=[(0,-1),(1,0),(0,1),(-1,0)]
        visisted_set=set()
        if originalcolor==color:
            return image
        queue=collections.deque([(sr,sc)])
        image[sr][sc]=color
        visisted_set.add((sr,sc))
        while queue:
            row,col=queue.popleft()
            visisted_set.add((row,col))
            for dr,dc in directions:
                nrow=row+dr
                ncol=col+dc
                if 0<=nrow<len(image) and 0<=ncol<len(image[0]) and image[nrow][ncol]==originalcolor:
                    image[nrow][ncol]=color
                    queue.append((nrow,ncol))
        return image


