class Solution:
    def reverseVowels(self, s: str) -> str:
        # implicit assumption: all strings are lowercase
        indices = []
        vowels = []
        vowel_set = {'a': 1, 'e': 1, 'i': 1, 'o': 1,
                     'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}

        for idx, char in enumerate(s):
            if char in vowel_set:
                vowels.append(char)
                indices.append(idx)

        s_split = list(s)
        vowels = vowels[::-1]
        for idx, index in enumerate(indices):
            s_split[index] = vowels[idx]

        return ''.join(s_split)
