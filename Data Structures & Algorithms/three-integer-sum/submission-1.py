class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        sums = []
        for i, n in enumerate(sorted_nums):
            if i > 0 and n == sorted_nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                diff = n + sorted_nums[l] + sorted_nums[r]
                if diff == 0:
                    sums.append([n, sorted_nums[l], sorted_nums[r]])
                    temp = l
                    while sorted_nums[l] == sorted_nums[temp] and l < r:
                        l += 1
                elif diff > 0:
                    r -= 1
                else:
                    l += 1
        return sums