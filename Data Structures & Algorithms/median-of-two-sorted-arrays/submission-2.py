class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = sorted(nums1 + nums2)

        mid = (len(sorted_nums) - 1) // 2
        if len(sorted_nums) % 2 == 0:
            return (sorted_nums[mid] + sorted_nums[mid + 1]) / 2
        else:
            return sorted_nums[mid]