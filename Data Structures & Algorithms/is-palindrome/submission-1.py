class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        alp = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        for i in s.lower():
            if i in alp:
                clean_s += i
        print(clean_s)
        r = len(clean_s) - 1
        for l in range(len(clean_s)):
            if clean_s[l] != clean_s[r]:
                return False
            r -= 1
        return True
