class Solution:
    def countBits(self, n: int) -> List[int]:
        def generateBinary(n, memo):
            binary = []
            initial = n
            while n:
                if n in memo:
                    binary.extend(memo[n])
                    break
                binary.append(n % 2)
                n = n // 2
            memo[initial] = binary
            return binary
        result = []
        memo = {}
        for i in range(0, n + 1):
            result.append(
                generateBinary(i, memo).count(1)
            )
        return result
