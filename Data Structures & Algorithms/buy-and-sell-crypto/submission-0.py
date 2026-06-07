class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        buy = 0
        sell = 1
        while buy < n and sell < n:
            max_profit = max(max_profit, prices[sell] - prices[buy])
            if prices[buy] >= prices[sell]:
                buy = sell
            sell += 1
        return max_profit