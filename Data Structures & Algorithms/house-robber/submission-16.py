class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2=nums[0]
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        prev2=nums[0]
        prev=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            pick=nums[i]+prev2
            notpick=prev
            current=max(pick,notpick)
            prev2=prev
            prev=current
        return prev
    
        