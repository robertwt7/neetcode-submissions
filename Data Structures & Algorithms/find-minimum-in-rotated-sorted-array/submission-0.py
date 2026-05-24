class Solution:
    def findMin(self, nums: List[int]) -> int:
        is_rotated = nums[0] > nums[-1]
        if not is_rotated:
            return nums[0]


        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            # if mid is bigger than the most right, that means that the lowest number is on the right area
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]