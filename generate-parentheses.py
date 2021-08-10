class Solution:
    def generateParenthesis(self, n: int):
        '''
        faster than 94.5% of Python solutions
        '''
        res = []

        def build(left, right, current_formation):
            if not left and not right:
                res.append(current_formation)
            else:
                if left:
                    build(left - 1, right, f'{current_formation}(')
                if right > left:
                    build(left, right - 1, f'{current_formation})')

        build(n, n, '')
        return list(set(res))

    # added dfs way of doing this in my second try
    def generateParenthesisDfs(self, n: int) -> List[str]:
        def dfs(results, acc, no_open, no_close):
            if no_open == 0 and no_close == 0:
                results.append(acc)
                return
            if no_close < 0 or no_open < 0:
                return
            if no_open == no_close:
                dfs(results, acc + '(', no_open - 1, no_close)
            else:
                dfs(results, acc + ')', no_open, no_close - 1)
                dfs(results, acc + '(', no_open - 1, no_close)

        results = []
        dfs(results, '', n, n)
        return results


soln = Solution()
print(soln.generateParenthesis(4))
