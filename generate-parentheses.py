class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(current_formation, remaining_count):
            if not remaining_count:
                res.append(current_formation)
            else:
                if remaining_count % 2 == 0 and current_formation:
                    dfs(f'{current_formation}{current_formation}',
                        remaining_count // 2 - 1)
                dfs(f'({current_formation})', remaining_count - 1)
                dfs(f'{current_formation}()', remaining_count - 1)
                dfs(f'(){current_formation}', remaining_count - 1)
        dfs('', n)
        return list(set(res))


soln = Solution()
print(soln.generateParenthesis(4))
