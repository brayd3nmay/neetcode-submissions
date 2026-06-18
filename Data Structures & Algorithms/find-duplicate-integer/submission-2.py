class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            number_index = abs(nums[i]) - 1
            if nums[number_index] < 0:
                return nums[i] if nums[i] > 0 else nums[i] * -1
            nums[number_index] *= -1