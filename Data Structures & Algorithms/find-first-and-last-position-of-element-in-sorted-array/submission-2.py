class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def floor(nums,target):
            low=0
            high=len(nums)-1
            result=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]<=target:
                    result=mid
                    low=mid+1

                else:
                    high=mid-1
            return result  
        def ciel(nums,target):
            low=0
            high=len(nums)-1
            result=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    result=mid
                    high=mid-1
                else:
                    low=mid+1
            return result
        floor=floor(nums,target)
        ciel=ciel(nums,target)
        if ciel>floor or ciel==-1:
            return [-1,-1]
        else:
            return [ciel,floor]       
        
        