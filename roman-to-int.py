class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        vals = list(map(lambda char: roman[char], s))
        temp = []
        res = 0
        for val in vals:
            if not temp:
                temp.append(val)
            elif val <= temp[-1]:
                res += sum(temp)
                temp = [val]
            elif val > temp[-1]:
                res += val - sum(temp)
                temp = []
            else:
                print('uncaught case')
        res += sum(temp)
        return res
    
soln = Solution()
print(soln.romanToInt('LVIII'))
print(soln.romanToInt('MCMXCIV'))
