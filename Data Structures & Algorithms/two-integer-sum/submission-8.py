class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index,value in enumerate(nums):
            sum=target-value
            if sum in dict:
                return[dict[sum],index]
            dict[value]=index


        
        