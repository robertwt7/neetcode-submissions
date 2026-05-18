from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        bucket = [[] for _ in nums]

        for n in nums:
            hm[n] += 1

        for key in hm:
            bucket[hm[key]-1].append(key)

        res = []
        for i in range(len(bucket)-1, -1, -1):
            res.extend(bucket[i])
            if len(res) == k:
                return res
        
        return res