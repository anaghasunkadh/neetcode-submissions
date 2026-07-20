class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k = (n - k % n) % n
        hashset={}
        for i in range(k):
            hashset[i]=nums[i]
        for i in range(k,n):
            nums[i-k]=nums[i]
        for i in range(k):
            nums[n-k+i]=hashset[i]