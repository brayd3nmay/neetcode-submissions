class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for temp in nums:
            count[temp] += 1

            if count[temp] > 1:
                return True

        return False