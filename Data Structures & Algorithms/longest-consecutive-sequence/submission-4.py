class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        seen=set(nums)
        length=0
        curr=0
        for num in seen:
            if num-1 not in seen:
                curr=num
                length=1
            while curr+1 in seen:
                curr=curr+1
                length+=1
            longest=max(length,longest)
        return longest

        