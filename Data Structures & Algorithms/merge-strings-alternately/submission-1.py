class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1=0
        pointer2=0
        result =""
        while pointer1<len(word1) and pointer2<len(word2):
            result+=word1[pointer1]
            pointer1=pointer1+1
            result=result+word2[pointer2]
            pointer2=pointer2+1
        if pointer1<len(word1):
            result=result+word1[pointer1:]
        if pointer2<len(word2):
            result=result+word2[pointer2:]
        return result