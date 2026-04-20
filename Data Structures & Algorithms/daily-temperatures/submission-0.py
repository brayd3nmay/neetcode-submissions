class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        num_days = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                num_days[index] = i - index
            stack.append(i)
        return num_days