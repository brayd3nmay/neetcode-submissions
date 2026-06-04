class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # char: last index it was seen
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in char_map:
                l = max(char_map[s[r]] + 1, l)
            longest = max(longest, r - l + 1)
            char_map[s[r]] = r
        return longest
