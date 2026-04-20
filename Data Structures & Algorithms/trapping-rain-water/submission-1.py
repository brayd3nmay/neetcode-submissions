class Solution:
    def trap(self, height: List[int]) -> int:
        curr_max = 0
        prefix = [0] * len(height)
        for i, h in enumerate(height):
            prefix[i] = curr_max
            curr_max = max(curr_max, h)

        curr_max = 0
        suffix = [0] * len(height) 
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = curr_max
            curr_max = max(curr_max, height[i])

        total_water = 0
        for i in range(len(height)):
            curr = min(prefix[i], suffix[i]) - height[i]
            total_water += max(0, curr)
        return total_water