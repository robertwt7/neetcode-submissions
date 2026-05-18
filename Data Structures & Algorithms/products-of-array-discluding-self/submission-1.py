class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1 for x in nums], [1 for x in nums]

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]
        return [suffix[i] * prefix[i] for i in range(0,len(nums))]