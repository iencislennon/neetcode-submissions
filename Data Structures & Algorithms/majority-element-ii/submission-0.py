class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        ans = []
       
        for i in d:
            if d[i] > int(len(nums)/3):
                ans.append(i)
        return ans