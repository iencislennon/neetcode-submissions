class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        target = 1
        while target in s:
            target += 1
        return target
        
   