class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        def isAna(A):
            dict={}
            for char in A:
                if char not in dict:
                    dict[char]=1
                else:
                    dict[char]+=1
            return dict
        for s in strs:
            count=isAna(s)
            key=tuple(sorted(count.items()))
            if key not in group:
                group[key]=[]
            group[key].append(s)
        return list(group.values())
        

        
        