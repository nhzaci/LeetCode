class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def memo_gen(numRows, memo):
            if numRows in memo:
                return memo[numRows]
            if numRows <= 0:
                return []
            if numRows == 1:
                return [[1]]
            if numRows == 2:
                return [[1], [1, 1]]

            prev_arr = self.generate(numRows - 1)
            prev = prev_arr[-1]
            curr = [0 for i in range(numRows)]
            curr[0] = 1
            curr[-1] = 1
            for i in range(1, numRows - 1):
                curr[i] = prev[i - 1] + prev[i]

            memo[numRows] = prev_arr + [curr]
            return memo[numRows]
        memo = {}
        res = memo_gen(numRows, memo)
        return res
