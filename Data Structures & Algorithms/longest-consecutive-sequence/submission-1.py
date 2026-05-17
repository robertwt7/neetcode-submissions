class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        my_set = set([])

        for n in nums:
            my_set.add(n)

        max_cons = 1
        for n in nums:
            if n+1 in my_set:
                continue
            elif n-1 in my_set:
                new_max = 1
                next_n = n-1
                while next_n in my_set:
                    new_max += 1
                    next_n -= 1
                max_cons = max(max_cons, new_max)
        return max_cons