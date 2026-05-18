from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            s_key = "".join(sorted(s))
            hm[s_key].append(s)

        return list(hm.values())
