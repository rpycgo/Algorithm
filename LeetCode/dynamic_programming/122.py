class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        hold = -prices[0]

        for price in prices[1:]:
            profit = max(profit, hold + price)
            hold = max(hold, profit - price)

        return profit
