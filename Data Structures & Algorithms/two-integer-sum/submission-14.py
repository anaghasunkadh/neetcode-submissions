class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index,value in enumerate(nums):
            comp=target-value
            if comp in dict:
                return [dict[comp],index]
            else:
                dict[value]=index
        