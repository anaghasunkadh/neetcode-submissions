class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        maxi=0
        right=len(heights)-1
        while left<right:
            h=min(heights[left],heights[right])
            w=right-left
            area=h*w
            if heights[left]<heights[right]:
                left=left+1
            else:
                right=right-1
            maxi=max(maxi,area)
        return maxi

        