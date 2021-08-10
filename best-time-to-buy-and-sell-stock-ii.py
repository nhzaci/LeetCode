class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 0, 0
        days = len(prices)
        while buy < days and sell < days:
            while buy < days - 1 and prices[buy] >= prices[buy + 1]:
                buy += 1

            sell = buy

            while sell < days - 1 and prices[sell] <= prices[sell + 1]:
                sell += 1

            profit += prices[sell] - prices[buy]
            buy = sell + 1
        return profit
