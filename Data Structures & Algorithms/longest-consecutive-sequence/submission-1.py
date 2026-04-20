class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for n in nums:
            if n - 1 not in nums_set:
                len = 1
                curr = n + 1
                while curr in nums_set:
                    len += 1
                    curr += 1
                longest = len if len > longest else longest
        return longest