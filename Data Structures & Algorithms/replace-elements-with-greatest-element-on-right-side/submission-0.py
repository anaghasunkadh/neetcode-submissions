class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxvalue=-1
        for i in range(len(arr)-1,-1,-1):
            value=arr[i]
            arr[i]=maxvalue
            maxvalue = max(maxvalue,value)
        return arr
            


        