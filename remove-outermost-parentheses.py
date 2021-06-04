class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # definition of outer parenthesis
        l_count = 0
        r_count = 0
        ptr = 0
        n = len(S)
        curr_str = ''
        result = ''
        while ptr < n:
            curr_str += S[ptr]
            if S[ptr] == '(':
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                result += curr_str[1:-1]
                curr_str = ''
            ptr += 1
        return result
