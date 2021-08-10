class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
                   'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        sorted_s1 = sorted(list(s1))
        sorted_s2 = sorted(list(s2))
        all_s1 = True
        all_s2 = True
        for idx in range(len(sorted_s1)):
            c1 = sorted_s1[idx]
            c2 = sorted_s2[idx]
            if letters[c1] < letters[c2]:
                all_s1 = False
            if letters[c2] < letters[c1]:
                all_s2 = False
            if not all_s1 and not all_s2:
                return False
        return all_s1 or all_s2
