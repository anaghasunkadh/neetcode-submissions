class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visisted_map_s = {}
        visisted_map_t={}
        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in visisted_map_s:
                visisted_map_s[s[i]]+=1
            else:
                visisted_map_s[s[i]]=1
            
        for i in range(len(t)):
            if t[i]  in visisted_map_t:
                visisted_map_t[t[i]]+=1
            else:
                visisted_map_t[t[i]]=1
        if visisted_map_s==visisted_map_t:
            return True
        return False
        


        
        