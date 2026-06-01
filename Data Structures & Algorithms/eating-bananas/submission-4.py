class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = max(piles)
        l, r = 0, min_speed
        while l <= r:
            m = l + ((r - l) // 2)
            if m == 0:
                break
            
            time = 0
            for p in piles:
                time += math.ceil(p / m)

                if time > h:
                    break
            
            if time > h:
                l = m + 1
            else:
                r = m - 1
                min_speed = min(min_speed, m)

        return min_speed
