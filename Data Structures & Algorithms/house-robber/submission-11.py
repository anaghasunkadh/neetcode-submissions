class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        prev2=nums[0]
        if n>1:
            prev=max(nums[0],nums[1])
            for i in range(2,n):
                pick=nums[i]+prev2
                notpick=prev
                curr =max(pick,notpick)
                prev2=prev
                prev=curr
            return prev
        else:
            return nums[0]
        
        
        
        

        