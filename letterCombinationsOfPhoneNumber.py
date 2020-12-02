class Solution:
    def letterCombinations(self, digits: str):
        '''
        Brute force solution -> iterate through all elements
        Worst case time complexity: O(n^2)
        Best case time complexity: O(n^2)
        '''
        hashmap = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: [
            'm', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u',  'v'], 9: ['w', 'x', 'y', 'z']}
        result = []

        for digit in digits:
            new_result = []

            # for character in array stored in hashmap
            for char in hashmap[int(digit)]:
                # if result initialised, iterate through result array
                if (len(result) > 0):
                    for other in result:
                        new_result.append(other + char)
                # else, initialise result array
                else:
                    new_result.append(char)
            # cache new result
            result = new_result

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("23"))
    print(solution.letterCombinations("2"))
    print(solution.letterCombinations(""))
