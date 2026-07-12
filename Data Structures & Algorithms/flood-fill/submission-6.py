class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visisted_set=set()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        original_color=image[sr][sc]
        queue=collections.deque()
        queue.append((sr,sc))
        image[sr][sc]=color
        while queue:
            row,col=queue.popleft()
            visisted_set.add((row,col))
            for r,c in directions:
                nrow=row+r
                ncol=col+c
                if  0<=nrow<len(image) and 0<=ncol<len(image[nrow]) and (nrow,ncol) not in visisted_set and image[nrow][ncol]==original_color:
                    image[nrow][ncol]=color
                    queue.append((nrow,ncol))
        return image

        