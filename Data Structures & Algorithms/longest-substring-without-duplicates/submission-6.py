class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                l += 1
                r = l
                seen.clear()

            longest = max(longest, r - l)
        return longest