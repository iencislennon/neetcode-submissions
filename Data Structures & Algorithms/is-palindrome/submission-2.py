class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp = "qwertyuiopasdfghjklzxcvbnm1234567890"
        clean_s = ""
        for i in s.lower():
            if i in alp:
                clean_s += i
        r = len(clean_s) -1 

        for l in range(len(clean_s)):
            if clean_s[l] != clean_s[r]:
                return False
            r -= 1
        return True 
