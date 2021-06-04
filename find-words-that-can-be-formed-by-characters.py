class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_table = {}
        # O(n)
        for char in chars:
            char_table[char] = char_table.get(char, 0) + 1
        
        total_length_can_be_formed = 0
        
        # O(n * m) 
        # n is hte number of words, 
        # m is the average length of words
        for word in words:
            can_form = True
            temp = char_table.copy()
            
            # O(m)
            for char in word:
                if char in temp:
                    if temp[char] > 0:
                        temp[char] -= 1
                        continue
                can_form = False
                break
                
            if can_form:
                total_length_can_be_formed += len(word)
        
        return total_length_can_be_formed
