class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_stack = []
        snw = []
        for c in s:
            if c.isalnum():
                snw.append(c)
        # length 4: abcd, mid = starts at 2 for popping
        # length 5: abcde, mid = 2, starts at 3 for popping
        mid = len(snw) // 2 if len(snw) % 2 == 0 else len(snw) // 2 + 1
        for i, x in enumerate(snw):
            if i >= mid:
                if len(s_stack) < 1:
                    return False
                c = s_stack.pop()
                if c.lower() != x.lower():
                    return False
            else:
                if len(snw) % 2 == 0:
                    s_stack.append(x)
                elif i != len(snw) // 2:
                    s_stack.append(x)

        return len(s_stack) == 0