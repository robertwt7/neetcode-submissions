from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        # sliding window, starting from the len of s1 where it was excluded before. so if len s1 is 3, len s2 is 4, then we start from index 3
        for i in range(len(s1), len(s2)):
            char_included = s2[i]
            char_excluded = s2[i - len(s1)]

            window_count[char_included] = window_count.get(char_included, 0) + 1
            window_count[char_excluded] -= 1

            if window_count[char_excluded] == 0:
                del window_count[char_excluded]

            if s1_count == window_count:
                return True
        
        return False