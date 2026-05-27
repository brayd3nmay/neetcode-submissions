class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            r = l
            str_len = 0
            while s[r] != "#":
                str_len = str_len * 10 + int(s[r])
                r += 1
            r += 1
            res.append(s[r : r + str_len])
            l = r + str_len
        return res