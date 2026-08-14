class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index,value in enumerate(nums):
            compliment=target-value
            if compliment in dict:
                return [dict[compliment],index]
            dict[value]=index

        