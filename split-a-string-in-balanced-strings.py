class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count = 0
        r_count = 0
        ptr = 0
        result = 0
        substrings = []
        while ptr < len(s):
            if s[ptr] == 'L':
                l_count += 1
            else:
                r_count += 1 
            if l_count == r_count and l_count > 0 and r_count > 0:
                result += 1
                l_count = 0
                r_count = 0
            ptr += 1
        return result
