class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = []
        window_maxes = []

        l = 0
        for r in range(len(nums)):
            l = r - k  + 1
            if deque and deque[0] < l:
                deque.pop(0)
            
            while len(deque) > 0 and nums[r] > nums[deque[-1]]:
                deque.pop()

            if len(deque) == 0 or nums[deque[-1]] >= nums[r]:
                deque.append(r)

            if l < 0:
                continue
            else:
                window_maxes.append(nums[deque[0]])
        
        return window_maxes