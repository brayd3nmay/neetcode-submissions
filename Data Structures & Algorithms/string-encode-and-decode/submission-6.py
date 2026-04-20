class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        print(encoded)

        return encoded
 
    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            j = s.find("#", i)
            i = j + int(s[i: j]) + 1
            j += 1
            decoded.append(s[j:i])
        return decoded