class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def build_freq(a):
            my_dict = {}
            for char in a:
                if char in my_dict:
                    my_dict[char]+=1
                else:
                    my_dict[char]=1
            return my_dict
        my_dict_s = build_freq(s)
        my_dict_t = build_freq(t)
        if my_dict_s == my_dict_t:
            return True
        else:
            return False

            
        
            

        