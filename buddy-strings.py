class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        a_not_same = []
        b_not_same = []
        two_char_same = False
        char_same = {}
        for i in range(len(a)):
            char_a = a[i]
            char_b = b[i]
            if char_a != char_b:
                a_not_same += [char_a]
                b_not_same += [char_b]
            else:
                char_same[char_a] = char_same.get(char_a, 0) + 1
                if char_same[char_a] >= 2:
                    two_char_same = True
        if len(a_not_same) == 2:
            return a_not_same[0] == b_not_same[-1] and a_not_same[-1] == b_not_same[0]
        elif len(a_not_same) > 0:
            return False
        else:
            return two_char_same
