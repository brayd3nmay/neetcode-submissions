class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for n in nums:
            if n + 1 not in nums:
                m = n
                while m - 1 in nums:
                    m -= 1
                longest = max(longest, n - m + 1)
        return longest