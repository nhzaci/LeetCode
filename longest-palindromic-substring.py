class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r, s, max_len=0, max_output=''):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    max_output = s[l:r + 1]
                l -= 1
                r += 1
            return (max_len, max_output)
            
        ptr = 0
        max_len = 0
        max_output = ''
        while ptr < len(s):
            
            # odd
            l = r = ptr
            a, b = isPalindrome(l, r, s)
            if a > max_len:
                max_len = a
                max_output = b
            
            # even
            l, r = ptr, ptr + 1
            a, b = isPalindrome(l, r, s)
            if a > max_len:
                max_len = a
                max_output = b
            
            ptr += 1
        
        return max_output
