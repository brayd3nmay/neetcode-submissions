class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                max_a = max(max_a, heights[l] * (r - l))
                l += 1
            else:
                max_a = max(max_a, heights[r] * (r - l))
                r -= 1
        return max_a