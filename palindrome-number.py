class Solution:
    def isPalindrome(self, x: int) -> bool:
        def checkPalindrome(i, j, item):
            while i >= 0 and j < len(item):
                if item[i] != item[j]:
                    return False
                i -= 1
                j += 1
            return True
                
        if x < 0:
            return False
        if len(str(x)) == 1:
            return True
        
        item = str(x)
        if len(item) % 2:
            # if odd
            mid = len(item) // 2
            return checkPalindrome(mid, mid, item)
        else:
            # even
            mid = len(item) // 2
            midMinusOne = mid - 1
            return checkPalindrome(midMinusOne, mid, item)
        
