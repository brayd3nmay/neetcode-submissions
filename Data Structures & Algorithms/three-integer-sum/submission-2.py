class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = [] 

        sorted_nums = sorted(nums)
        for i, n in enumerate(sorted_nums):
            if i > 0 and n == sorted_nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = n + sorted_nums[l] + sorted_nums[r]

                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    triplets.append([n, sorted_nums[l], sorted_nums[r]])

                    l += 1 
                    while l < len(nums) and sorted_nums[l - 1] == sorted_nums[l]:
                        l += 1

        return triplets