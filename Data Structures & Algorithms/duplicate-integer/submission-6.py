class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
            if counts[n] > 1:
                return True

        return False