from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        for left, c in enumerate(s2):
            hm = Counter(s1)
            if c in hm:
                right = left + len(s1)
                if right > len(s2):
                    return False

                counter = 0
                for i in range(left, right):
                    if s2[i] in hm:
                        hm[s2[i]] -= 1
                        if hm[s2[i]] == 0:
                            del hm[s2[i]]
                    else:
                        break
                if not hm:
                    return True
        
        return False