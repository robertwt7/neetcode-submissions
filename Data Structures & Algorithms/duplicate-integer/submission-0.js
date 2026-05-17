class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const dict = {}

        for (let i = 0; i < nums.length; i++) {
            if (dict?.[nums[i]] === 1) {
                return true
            } else {
                dict[nums[i]] = 1
            }
        }

        return false
    }
}
