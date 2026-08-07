class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        order={}
        def isAna(A):
            dict={}
            for char in A:
                if char not in dict:
                    dict[char]=1
                else:
                    dict[char]+=1
            return dict
        for s in strs:
            val=isAna(s)
            count=tuple(sorted(val.items()))
            if count not in order:
                order[count]=[]
            
            order[count].append(s)
        return list(order.values())


        