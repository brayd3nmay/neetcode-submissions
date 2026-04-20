class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        while l <= r:
            if max_l <= max_r:
                total_water += max(0, max_l - height[l])
                max_l = max(max_l, height[l])
                l += 1
            else:
                total_water += max(0, max_r - height[r])
                max_r = max(max_r, height[r])
                r -= 1
        return total_water