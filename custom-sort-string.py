class Solution:
    def customSortString(self, S: str, T: str) -> str:
        res = T
        for char in S[-1::-1]:
            if char in T:
                res = char * T.count(char) + ''.join(res.split(char))
        return res
