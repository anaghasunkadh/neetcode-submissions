class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_img=image[sr][sc]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visisted_set=set()
        queue=collections.deque()
        if (sr,sc) not in visisted_set:
            queue.append((sr,sc))
            visisted_set.add((sr,sc))
        image[sr][sc]=color
        while queue:
            row,col=queue.popleft()
            for dr,dc in directions:
                nr=row+dr
                nc=col+dc
                if 0<=nr<len(image) and 0<=nc<len(image[nr]) and (nr,nc) not in visisted_set and image[nr][nc]==original_img:
                    image[nr][nc]=color
                    queue.append((nr,nc))
                    visisted_set.add((nr,nc))
        return image
        