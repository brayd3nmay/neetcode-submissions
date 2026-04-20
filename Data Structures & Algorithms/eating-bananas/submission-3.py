class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        min_time = max_pile
        l, r = 0, max_pile
        while l <= r:
            m = (l + r) // 2

            if m == 0:
                break

            time = 0 
            for p in piles:
                time += math.ceil(p / m) 
                if time > h:
                    break

            if time <= h:
                min_time = min(min_time, m)
                r = m - 1
            else:
                l = m + 1
        return min_time