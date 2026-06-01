class TimeMap:
    TIME = 0
    VAL = 1

    def __init__(self):
        self.maps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.maps:
            map = self.maps[key]

            l, r = 0, len(map) - 1
            while l <= r:
                m = l + ((r - l) // 2)

                time = map[m][0]
                if time == timestamp:
                    return self.maps[key][m][1]
                elif time < timestamp:
                    res = map[m][1]
                    l = m + 1
                else:
                    r = m - 1

        return res 
