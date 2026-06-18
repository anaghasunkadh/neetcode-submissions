class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_dict = {}
        for i in range(len(nums)):
            value = target-nums[i]
            if value in visited_dict:
                return [visited_dict[value],i]
            else:
                visited_dict[nums[i]]=i

        