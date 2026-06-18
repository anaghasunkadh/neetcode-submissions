class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftsum =0
        rightsum=0
        maxsum=0
        n=len(cardPoints)
        for i in range(0,k):
            leftsum=leftsum+cardPoints[i]
            maxsum=max(maxsum,leftsum+rightsum)
        for i in range(0,k):
            leftsum = leftsum-cardPoints[k-1-i]
            rightsum=rightsum+cardPoints[n-1-i]
            maxsum=max(maxsum,leftsum+rightsum)
        return maxsum



        