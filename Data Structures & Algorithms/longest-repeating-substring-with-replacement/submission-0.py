class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        char_freq = defaultdict(int)
        l = 0
        for r in range(len(s)):
            print(f"l: {l}, r: {r}, longest: {longest}")
            char_freq[s[r]] += 1
            # window size - size of most freq char
            while (r - l + 1) - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest 