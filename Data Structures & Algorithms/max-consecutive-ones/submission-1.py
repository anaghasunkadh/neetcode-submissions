class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        low=0
        count=0
        maxCount=0
        for high in range(len(nums)):
            if nums[high]==1:
                count+=1
                maxCount=max(maxCount,count)
            else:
                if nums[high]==0:
                    count=0
        return maxCount
        
        