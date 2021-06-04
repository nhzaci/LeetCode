class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def convertToBits(number, curr=''):
            if number == 0:
                return curr
            else:
                return convertToBits(number // 2, str(number % 2) + curr)
        x_bits, y_bits = convertToBits(x), convertToBits(y)
        max_len = max(len(x_bits), len(y_bits))
        x_bits = '0' * (max_len - len(x_bits)) + x_bits
        y_bits = '0' * (max_len - len(y_bits)) + y_bits
        
        return len(list(filter(lambda xBityBit: xBityBit[0] != xBityBit[1], zip(x_bits, y_bits))))
