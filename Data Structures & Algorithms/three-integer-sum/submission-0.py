class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
                
            j, k = i + 1, len(nums) - 1
            while j < k:
                if sorted_nums[i] * -1 == sorted_nums[j] + sorted_nums[k]:
                    sums.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                elif sorted_nums[i] * -1 > sorted_nums[j] + sorted_nums[k]:
                    j += 1
                else:
                    k -= 1

        return sums