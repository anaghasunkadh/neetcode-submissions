class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            left=nums[mid-1] if mid-1>=0 else None
            right=nums[mid+1] if mid+1<len(nums) else None
            if left!=nums[mid] and right!=nums[mid]:
                return nums[mid]
            elif left==nums[mid]:
                if (mid-1)%2==1:
                    high=mid-2
                else:
                    low=mid+1
            else:
                if (mid+1)%2==1:
                    low=mid+2
                else:
                    high=mid-1
            

        
        