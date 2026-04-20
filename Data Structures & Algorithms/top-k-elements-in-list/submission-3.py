class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        freq = [[] for _ in range(len(nums))]
        for n, f in freq_map.items():
            freq[f - 1].append(n)
        
        res = []
        while k > 0:
            if freq[len(freq) - 1]:
                res.append(freq[len(freq) - 1].pop())
                k -= 1
            else:
                freq.pop()
        return res