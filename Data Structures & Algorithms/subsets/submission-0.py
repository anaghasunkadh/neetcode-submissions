class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def f(nums,i,ds):
            if(i==len(nums)):
                ans.append(list(ds))
                return
            ds.append(nums[i])
            f(nums,i+1,ds)
            ds.pop()
            f(nums,i+1,ds)
        f(nums,0,[])
        return ans
    

        