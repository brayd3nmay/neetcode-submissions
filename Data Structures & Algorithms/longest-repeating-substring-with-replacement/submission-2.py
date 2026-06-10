class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        curr_freq = {}
        l = 0
        for r in range(len(s)):
            print(f"r: {r}")
            curr_freq[s[r]] = curr_freq.get(s[r], 0) + 1
            print(f"curr_freq: {curr_freq}")
            while sum(curr_freq.values()) - max(curr_freq.values()) > k:
                print(f"while l: {l}")
                curr_freq[s[l]] -= 1
                l += 1
            print(f"l before res: {l}")
            res = max(res, r - l + 1)
            print(f"res: {res}")
            
        return res