class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        max_l, max_r = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                area += max_l - height[l] if max_l - height[l] > 0 else 0
                max_l = max(max_l, height[l])
                l += 1
            else:
                area += max_r - height[r] if max_r - height[r] > 0 else 0
                max_r = max(max_r, height[r])
                r -= 1
        return area