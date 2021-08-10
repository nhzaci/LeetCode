class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for idx in range(n):
            for i in range(idx + 1, n):
                if prices[i] <= prices[idx]:
                    prices[idx] -= prices[i]
                    break
        return prices
