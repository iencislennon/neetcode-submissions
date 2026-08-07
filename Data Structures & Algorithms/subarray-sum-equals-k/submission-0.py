class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        cur_sum = 0
        result = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            need_sum = cur_sum - k
            if need_sum in d:
                result += d[need_sum]
            d[cur_sum] = d.get(cur_sum, 0) + 1
        return result
