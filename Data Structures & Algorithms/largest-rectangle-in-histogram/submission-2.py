class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for i, h in enumerate(heights):
            start_idx = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                largest = max(largest, height * (i - index))
                start_idx = index
            stack.append([start_idx, h])
        
        for i, h in stack:
            largest = max(largest, h * (len(heights) - i))
        return largest
