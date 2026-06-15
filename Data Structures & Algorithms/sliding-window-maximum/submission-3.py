from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # indexes
        window_maxes = []

        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if (r + 1) >= k:
                window_maxes.append(nums[q[0]])
                l += 1
        
        return window_maxes