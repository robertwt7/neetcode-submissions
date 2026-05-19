class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}:{s}"
        
        return encoded
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        decoded = []
        n_to_read = 0
        c = 0
        while c < len(s):
            if s[c] == ":":
                new_s = ""
                for _ in range(n_to_read):
                    c += 1
                    new_s += s[c]
                decoded.append(new_s)
                n_to_read = 0
            else:
                n_to_read = n_to_read + int(s[c]) if n_to_read == 0 else n_to_read * 10 + int(s[c])
            c += 1

        return decoded

