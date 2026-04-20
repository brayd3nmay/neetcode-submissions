class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)
        fleets = []

        for p, s in cars:
            time = (target - p) / s
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        return len(fleets)