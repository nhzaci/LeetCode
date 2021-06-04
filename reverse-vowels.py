class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}
        indices = []
        vowels = []
        for idx, char in enumerate(s):
            if char in vowel:
                vowels += [char]
                indices += [idx]
        final_str = list(s)
        for i in range(len(indices)):
            final_str[indices[i]] = vowels[-(i + 1)]
        return ''.join(final_str)
