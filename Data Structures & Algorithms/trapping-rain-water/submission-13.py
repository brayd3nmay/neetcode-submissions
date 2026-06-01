class Solution:
    def trap(self, height: List[int]) -> int:
        # Time: O(n) Space: O(1)

        if not height:
            return 0

        area = 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                area += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                area += right_max - height[r]
        return area
