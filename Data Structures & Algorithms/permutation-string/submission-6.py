from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_c = Counter(s2[:len(s1)])

        if window_c == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            excluded_i = s2[i - len(s1)]
            window_c[excluded_i] -= 1
            window_c[s2[i]] = window_c.get(s2[i], 0) + 1

            if window_c[excluded_i] == 0:
                del window_c[excluded_i]

            if window_c == s1_count:
                return True

        return False
            
