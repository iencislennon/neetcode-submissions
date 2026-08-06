class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for i in s:
            if i-1 not in s: #start ig or sum
                num = i 
                cnt = 1
                while num + 1 in s:
                    num += 1
                    cnt += 1
                longest = max(cnt, longest)
        return longest
                        
