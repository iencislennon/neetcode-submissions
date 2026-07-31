class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0 
        k = 0
        for l in range(len(nums)):
            if nums[l] != val:
                nums[l], nums[r] = nums[r], nums[l]
                r += 1 
                k+= 1
        return k 
                
