class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in num_set:
                m = n
                while m in num_set:
                    m += 1
                longest = max(longest, m - n)
        return longest