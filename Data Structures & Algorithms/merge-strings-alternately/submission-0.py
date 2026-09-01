class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = 0
        ans = ""
        for l in range(len(word1)+len(word2)):
            if l < len(word1):
                ans += word1[l]
            if r < len(word2):
                ans += word2[r]
                r+= 1
        return ans            
            