class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        num1 = ('0' * (max_len - len(num1)) + num1)[::-1]
        num2 = ('0' * (max_len - len(num2)) + num2)[::-1]
        ptr = 0
        result = ''
        carry = 0
        while ptr < len(num1) or ptr < len(num2) or carry:
            v1 = v2 = 0
            if ptr < len(num1):
                v1 = int(num1[ptr])
            if ptr < len(num2):
                v2 = int(num2[ptr])
            print(v1, v2)
            print(carry)
            s = v1 + v2 + carry
            carry = s // 10
            s %= 10
            result = str(s) + result
            ptr += 1
        return result
                
