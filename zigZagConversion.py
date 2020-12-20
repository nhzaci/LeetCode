import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [['' for i in range(len(s))] for i in range (numRows)]
        str_idx = 0 # pointer for string index
        break_cond = False # for breaking out of loop
        if len(s) == 1 or numRows == 1:
            return s
        
        # generate palindrome
        for i in range(len(matrix[0])): # i = cols
            # determine gaps between rows are zigzags and full rows
            if not i % (numRows - 1):
                # fill col completely if i % (numRows - 1) == 0
                for j in range(numRows): # j = rows
                    matrix[j][i] = s[str_idx]
                    str_idx += 1
                    if str_idx == len(s):
                        break_cond = True
                        break
            else:
                # determine which row to be filled
                j = numRows - 1 - (i % (numRows - 1))
                matrix[j][i] = s[str_idx]
                str_idx += 1
            
            if str_idx == len(s) or break_cond:
                break
        
        result = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result += matrix[i][j]
        return result
