class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        sorted_freq = list(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        top_k = [item for item, freq in sorted_freq[0:k]]
        return top_k