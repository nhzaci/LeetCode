class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # n = amount
        # m = len(coins)
        # time complexity: O(n * m) -> n iterations of m coins each
        # space complexity: O(n) -> n length array to tabulate
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
