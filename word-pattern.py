class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = {}
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        exist_word_dict = {}
        for (index, char) in enumerate(pattern):
            if char in word_dict:
                if words[index] != word_dict[char]:
                    return False
            else:
                if words[index] not in exist_word_dict:
                    word_dict[char] = words[index]
                    exist_word_dict[words[index]] = 1
                else:
                    return False
                
        return True
