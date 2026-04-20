class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        temp = 1
        for i, n in enumerate(nums):
            pre[i] = temp
            temp *= n

        post = [1] * len(nums)
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = temp
            temp *= nums[i]

        products = [1] * len(nums)
        for i in range(len(nums)):
            products[i] = pre[i] * post[i]
        return products