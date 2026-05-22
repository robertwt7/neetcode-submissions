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

        first_h = snw[0:len(snw)//2]
        second_h = snw[mid:]

        for x in second_h:
            if first_h.pop().lower() != x.lower():
                return False

        return True