from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hm = defaultdict(int)
        for c in s1:
            hm[c] += 1

        left = 0
        
        # start the window with the length of s1
        # if length s1 is 3, then we want to limit the inner loop to 3 as well
        for right in range(len(s1), len(s2) + 1):
            ref_hm = hm.copy()
            for i in range(left, right):
                if s2[i] not in ref_hm:
                    break
                else:
                    ref_hm[s2[i]] -= 1
                    if ref_hm[s2[i]] == 0:
                        del ref_hm[s2[i]]
            
            if len(ref_hm) == 0:
                return True
            left += 1
        return False