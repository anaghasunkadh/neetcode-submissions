class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalcolor=image[sr][sc]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        visisted_set=set()
        queue=collections.deque()
        queue.append((sr,sc))
        image[sr][sc]=color
        while queue:
            row,col=queue.popleft()
            visisted_set.add((row,col))
            for dr,dc in directions:
                nrow=row+dr
                ncol=col+dc
                if 0<=nrow<len(image) and 0<=ncol<len(image[nrow]) and image[nrow][ncol]==originalcolor and (nrow,ncol) not in visisted_set:
                    image[nrow][ncol]=color
                    queue.append((nrow,ncol))
        return image

        