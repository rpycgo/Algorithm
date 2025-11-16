class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)

            hold, sold, rest = new_hold, new_sold, new_rest

        answer = max(sold, rest)

        return answer
