class TimeMap:

    def __init__(self):
       self.time_map = defaultdict(list) # key : list of [time, val]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key, [])
        res = ""

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2

            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] < timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res