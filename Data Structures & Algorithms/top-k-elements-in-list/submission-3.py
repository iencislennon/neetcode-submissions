class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # частота
        freq = {}
        for val in nums:
            freq[val] = freq.get(val, 0) + 1
        
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])

        for num, count in freq.items():
            buckets[count].append(num)

        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans

        