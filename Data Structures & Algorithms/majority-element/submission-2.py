class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        for i in nums:
            if d.get(i) > n//2:
                return i 
        
