from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        hm = defaultdict(int)
        max_window = 0
        while right < len(s):
            hm[s[right]] += 1
            if hm[s[right]] > 1:
                while hm[s[right]] > 1:
                    hm[s[left]] -= 1
                    left += 1
            max_window = max(max_window, right - left + 1)
            right += 1
        
        return max_window