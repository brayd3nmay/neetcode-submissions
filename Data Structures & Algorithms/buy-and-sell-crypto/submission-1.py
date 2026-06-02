class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for p in prices:
            while prices[buy] > p:
                buy += 1
            
            if prices[buy] < p:
                profit = max(profit, p - prices[buy])
        return profit