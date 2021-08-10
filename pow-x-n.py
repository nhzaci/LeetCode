class Solution:
    # Time complexity: O(log2 n) -> we halve n each time
    # Space complexity: O(log2 n)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        elif n > 0:
            return x * self.myPow(x * x, n // 2)
        else:
            return 1 / self.myPow(x, -n)
