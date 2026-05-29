class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        sorted_cars = sorted(cars, reverse=True) # sorted high to low by position

        stack = [] # stack of arrival times
        for pos, speed in sorted_cars: 
            time = (target - pos) / speed
            if not stack:
                stack.append(time)

            if stack and time > stack[-1]:
                stack.append(time)
        return len(stack)