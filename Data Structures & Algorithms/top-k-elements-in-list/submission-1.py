class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for i in nums:
            d[i] = 1 + d.get(i, 0)

        buckets = []
        for i in range (len(nums)+1):
            buckets.append([])
        for i, val in d.items():
            buckets[val].append(i)
    
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans               
        return ans
        