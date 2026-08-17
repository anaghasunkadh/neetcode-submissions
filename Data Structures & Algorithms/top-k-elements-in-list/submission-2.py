class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        res=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]=count.get(num,0)+1
        for value,c in count.items():
            res[c].append(value)
        r=[]
        for i in range(len(res)-1,0,-1):
            for n in res[i]:
                r.append(n)
                if len(r)==k:
                    return r

        