class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        fst, sec, trd = 0, 1, 1
        for i in range(3, n + 1):
            fst, sec, trd = sec, trd, fst + sec + trd

        return trd
