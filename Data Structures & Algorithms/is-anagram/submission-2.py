class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d_t = {}
        d_s = {}
        for i in s:
            if i not in d_s:
                d_s[i] = 0
            else:
                d_s[i] += 1 
        for i in t:
            if i not in d_t:
                d_t[i] = 0
            else:
                d_t[i] += 1

        for letter in d_s:
            if d_s.get(letter, "A") != d_t.get(letter, "A"):
                return False
        return True


        