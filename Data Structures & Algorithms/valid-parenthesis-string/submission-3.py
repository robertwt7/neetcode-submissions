class Solution:
    def checkValidString(self, s: str) -> bool:
        left_p = []
        star = []

        for i, c in enumerate(s):
            if c == "(":
                left_p.append(i)
            elif c == "*":
                star.append(i)
            else:
                if len(left_p):
                    left_p.pop()
                elif len(star):
                    star.pop()
                else:
                    return False
        
        if len(left_p) > len(star):
            return False
        
        while len(left_p):
            lp_i = left_p.pop()
            s_i = star.pop()

            if s_i < lp_i:
                return False

        return True