class Solution:
    def fib(self, n: int) -> int:
        # fib with memoized results
        memo = {0: 0, 1: 1}

        def fib_helper(i):
            nonlocal memo
            if i in memo:
                return memo[i]
            if i < 0:
                return 0
            else:
                memo[i] = fib_helper(i - 1) + fib_helper(i - 2)
                return memo[i]

        if n in memo:
            return memo[n]
        else:
            return fib_helper(n)


soln = Solution()
print(soln.fib(10))
print(soln.fib(9))
print(soln.fib(7))
