class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        length=0
        longest=0
        for num in seen:
            if num-1 not in seen:
                length=1
                curr=num
                while curr+1 in seen:
                    length=length+1
                    curr=curr+1
                longest=max(length,longest)
        return longest
