class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # naive solution
        dict_of_words = {}
        for i in range(len(A)):
            for char in A[i]:
                dict_of_words[i] = dict_of_words.get(i, {})
                dict_of_words[i][char] = dict_of_words[i].get(char, 0) + 1
        
        final_list = {char: 0 for char in string.ascii_lowercase}
        for char in final_list:
            all_dicts_count = list(map(lambda idx: dict_of_words.get(idx, {}).get(char, 0), range(len(A))))
            if all(all_dicts_count):
                final_list[char] = min(all_dicts_count)
        
        result = ''
        for char, times in final_list.items():
            result += char * times
        return result
