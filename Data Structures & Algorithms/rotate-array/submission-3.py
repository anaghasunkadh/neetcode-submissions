class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=(n+k-n)%n
        nums[:]=nums[::-1]
        nums[0:k]=nums[0:k][::-1]
        nums[k:n]=nums[k:n][::-1]
        