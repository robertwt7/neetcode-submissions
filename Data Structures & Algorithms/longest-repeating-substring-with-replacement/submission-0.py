from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        left = 0

        max_length = 0
        for end, c in enumerate(s):
            hm[c] += 1

            # calculate if we are already replacing at most K
            while end - left + 1 - max(hm.values()) > k:
                hm[s[left]] -= 1
                left += 1

            max_length = max(max_length, end - left + 1)
        return max_length