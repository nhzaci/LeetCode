class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # n = len(t)
        # m = len(s)
        # time complexity: O(n * m) -> worst case we iterate through n for each m
        # space complexity: O(1) -> no extra space required
        # pointer on s for current character
        # pointer on t to iterate through t and find the next character
        # if pointer on t reaches the end and pointer on s != len(s) => False
        # else True
        pS = 0
        pT = 0
        nS = len(s)
        nT = len(t)
        while pS < nS and pT < nT:
            # equal => advance both pointers
            if s[pS] == t[pT]:
                pS += 1
                pT += 1
            else:
                # advance ptr on t
                pT += 1
        return pS == nS
