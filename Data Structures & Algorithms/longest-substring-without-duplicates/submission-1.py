from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        last_seen = defaultdict(int)
        max_window = 0
        for end, c in enumerate(s):
            if c in last_seen and last_seen[c] >= start:
                start = last_seen[c] + 1
            
            last_seen[c] = end
            max_window = max(max_window, end - start + 1)
        
        return max_window