class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        char_freq = defaultdict(int)

        max_freq = 0
        l = 0
        for r in range(len(s)):
            char_freq[s[r]] += 1
            max_freq = max(max_freq, char_freq[s[r]])
            while (r - l + 1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest 