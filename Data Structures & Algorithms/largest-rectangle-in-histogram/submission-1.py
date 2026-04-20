class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                largest_area = max(largest_area, height * (i - index))
                start = index
            stack.append([start, h]) # height and position

        for s, h in stack:
            largest_area = max(largest_area, h * (len(heights) - s))
        return largest_area