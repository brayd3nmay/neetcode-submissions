class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)
        fleets = []

        for p, s in cars:
            time = (target - p) / s
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        return len(fleets)