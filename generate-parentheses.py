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


soln = Solution()
print(soln.generateParenthesis(4))
