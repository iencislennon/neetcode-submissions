class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d_t = {}
        d_s = {}

        for i in range(len(s)):
            d_t[t[i]] = 1 + d_t.get(t[i], 0)
            d_s[s[i]] = 1 + d_s.get(s[i], 0)

        for letter in d_t:
            if d_t[letter] != d_s.get(letter, "A"):
                return False 
        return True 



        