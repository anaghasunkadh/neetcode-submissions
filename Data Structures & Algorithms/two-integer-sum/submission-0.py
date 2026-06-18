class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visisted_dict = {}
        
        for i in range(len(nums)):
            value = target-nums[i]
            if value in visisted_dict:
                ls = [visisted_dict[value],i]
            visisted_dict[nums[i]]=i
            
            
        return ls

        
        