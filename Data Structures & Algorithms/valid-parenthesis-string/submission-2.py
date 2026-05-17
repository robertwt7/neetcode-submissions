class Solution:
    def checkValidString(self, s: str) -> bool:
        left_p = []
        star = []
        for i, x in enumerate(s):
            if x == "(":
                left_p.append(i)
            elif x == "*":
                star.append(i)
            else:
                if len(left_p) > 0:
                    left_p.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
        
        if len(left_p) > len(star):
            return False

        while(len(left_p)):
            p_index = left_p.pop()
            s_index = star.pop()
            # means that s comes before the P, invalid!
            if s_index < p_index:
                return False
            
        return True