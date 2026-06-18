class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            value=target-nums[i]
            if value not in dict:
                dict[nums[i]]=i
            else:
                return [dict[value],i]
        