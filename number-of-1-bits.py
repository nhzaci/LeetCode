class Solution:
    def hammingWeight(self, n: int) -> int:
        def convertToBinary(n, curr=''):
            if n == 0:
                return curr
            else:
                return convertToBinary(n // 2, str(n % 2) + curr)
        return sum(map(lambda x: x == '1', convertToBinary(n)))
