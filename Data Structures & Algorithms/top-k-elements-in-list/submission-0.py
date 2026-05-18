from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for n in nums:
            hm[n] += 1
        
        dict_sorted = sorted(list(hm.items()), reverse=True, key=lambda x: x[1])

        return [dict_sorted[x][0] for x in range(0, k)]