import bisect
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            # mid is the number of hours we're looking for
            mid = left + (right - left) //  2

            # each time we divide with the speed, we need to do ceil because that takes at least extra hour
            hours_needed = sum(math.ceil(pile / mid) for pile in piles)
            if hours_needed <= h:
                # find the lower one if there's any
                right = mid
            else:
                left = mid + 1

        # we have converge so left == right
        return left