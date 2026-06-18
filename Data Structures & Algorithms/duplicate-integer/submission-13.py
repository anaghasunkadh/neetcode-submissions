class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valid_set = set()
        for num in nums:
            if num in valid_set:
                return True
            valid_set.add(num)
        return False
        