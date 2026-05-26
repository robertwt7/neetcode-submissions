from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        max_f = 0
        left = 0

        longest = 0
        for end, c in enumerate(s):
            hm[c] += 1
            max_f = max(max_f, hm[c])

            while end - left + 1 - max_f > k:
                hm[s[left]] -= 1
                left += 1

            longest = max(longest, end - left + 1)
        
        return longest