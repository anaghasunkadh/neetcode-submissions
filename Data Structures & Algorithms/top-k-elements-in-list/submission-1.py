import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        dict={}
        for num in nums:
            dict[num]=dict.get(num,0)+1
        for num,count in dict.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count,num in heap]

        