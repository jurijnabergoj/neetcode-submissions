class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        curr_profit = 0

        for p in prices:
            if p > curr_min:
                profit = p - curr_min
                if profit > curr_profit:
                    curr_profit = profit
            else:
                curr_min = p
        return curr_profit