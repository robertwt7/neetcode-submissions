class Solution:
    def isValid(self, s: str) -> bool:
        o_stack = []
        closing = [')', ']', '}']
        hm = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for x in s:
            if x not in closing:
                o_stack.append(x)
            else:
                if len(o_stack) < 1 or o_stack.pop() != hm[x]:
                    return False
        
        return len(o_stack) == 0