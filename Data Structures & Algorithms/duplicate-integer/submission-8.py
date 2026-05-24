class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}
        for n in nums:
            if n in freq_map:
                return True
            else:
                freq_map[n] = 1
        return False