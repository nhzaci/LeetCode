class Solution:
    # time complexity: O(n) -> O(1) for O(n) recursive calls
    # space complexity: O(n) -> n recursive calls
    def makeGood(self, s: str, curr_idx=0) -> str:
        if curr_idx > len(s) - 2:
            return s

        for index in range(curr_idx, len(s) - 1):
            character = s[index]
            next_char = s[index + 1]
            if (character.upper() == next_char or next_char.upper() == character) and character != next_char:
                return self.makeGood(s[:index] + s[index + 2:], max(0, index - 1))
        return s
