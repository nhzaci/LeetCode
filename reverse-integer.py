class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        new_str = ''
        for char in str(abs_x):
            new_str = char + new_str

        if int(new_str) > 2 ** 31:
            return 0

        return -int(new_str) if x < 0 else int(new_str)
