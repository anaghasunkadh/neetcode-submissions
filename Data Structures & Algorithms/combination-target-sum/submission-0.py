class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def f(i,nums,target,ds):
            if i>=len(nums):
                if target==0:
                    ans.append(list(ds))
                return
            if target>0:
                ds.append(nums[i])
                f(i,nums,target-nums[i],ds)
                ds.pop()
            f(i+1,nums,target,ds)
        f(0,nums,target,[])
        return ans
            


        