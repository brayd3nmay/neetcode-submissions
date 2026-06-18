class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            num_idx = abs(n) - 1
            if nums[num_idx] < 0:
                return abs(n)
            nums[num_idx] *= -1
        return -1
