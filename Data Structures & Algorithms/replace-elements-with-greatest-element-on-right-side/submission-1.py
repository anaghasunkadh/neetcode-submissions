class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest=-1
        for i in range(len(arr)-1,-1,-1):
            value=arr[i]
            arr[i]=largest
            largest=max(largest,value)
        return arr
                
        

        