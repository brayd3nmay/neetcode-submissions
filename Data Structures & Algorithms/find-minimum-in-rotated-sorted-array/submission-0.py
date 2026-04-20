class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = math.inf
        while l <= r:
            m = (l + r) // 2

            res = min(res, nums[m])
            if nums[r] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res