class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))

        res = 0
        curr_pos = 0
        for pos, speed in sorted(cars, reverse=True):
            if ((target - pos) / speed) > curr_pos:
                res += 1
                curr_pos = ((target - pos) / speed)
        return res