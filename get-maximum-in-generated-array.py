class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # time complexity: O(n) -> O(n) time
        # spcae complexity: O(n) -> O(n) memoization to store prev values
        if n == 0:
            return 0
        if n == 1:
            return 1

        store = [0 for i in range(n + 1)]
        store[1] = 1
        prev = 1
        max_val = 1

        for i in range(2, n + 1):
            if i == prev * 2:
                store[i] = store[prev]
            elif i == prev * 2 + 1:
                store[i] = store[prev] + store[prev + 1]
            elif i >= (prev + 1) * 2:
                prev = prev + 1
                if i == (prev + 1) * 2 + 1:
                    store[i] = store[prev] + store[prev + 1]
                else:
                    store[i] = store[prev]
            max_val = max(max_val, store[i])

        return max_val
