class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        min_price = 100000 # max_price = 10^4, so 10^5 is inf
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
