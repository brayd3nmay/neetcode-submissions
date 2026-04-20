class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#"
            encoded += s
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        w, i = 0, 0
        while i < len(s):
            while s[i] != "#":
                w = w * 10 + int(s[i])
                i += 1
            i += 1
            word = s[i: i + w]
            decoded.append(word)
            i += w
            w = 0
        return decoded