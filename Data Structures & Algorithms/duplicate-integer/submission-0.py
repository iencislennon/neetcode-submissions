class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, val in enumerate(nums):
            if val not in d:
                d[val] = i
            else:
               return True 
        return False