class Solution:

    def rob(self, nums: List[int]) -> int:
        def rob_linear(modified_nums: List[int]):
            prev2 = modified_nums[0]
            prev1 = max(modified_nums[0], modified_nums[1])

            for i in range(2, len(modified_nums)):
                current = max(prev1, modified_nums[i] + prev2)
                prev2 = prev1
                prev1 = current
            
            return prev1
        if len(nums) <= 2:
            return max(nums)
        result1 = rob_linear(nums[1:])
        result2 = rob_linear(nums[:-1])

        return max(result1, result2)

