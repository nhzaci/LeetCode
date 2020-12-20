from DataStructures.unionFindDataStructure import UFDS


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Sliding window solution, keep iterating from 0 onwards, 1 onwards, etc
        Best case time complexity: O(n) -> Single distinct whole substring
        Worst case time complexity: O(n^2) -> Repeating character at the end of the substring
        '''
        max_count = 0
        hashtable = {}
        start_index = 0

        if len(s) == 1:
            return 1

        while start_index < len(s):
            hashtable = {}
            curr_count = 0

            for idx in range(start_index, len(s)):
                if s[idx] in hashtable:
                    max_count = max(max_count, curr_count)
                    break
                else:
                    curr_count += 1
                    hashtable[s[idx]] = 1
                max_count = max(max_count, curr_count)

            start_index += 1

        return max_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abc'))
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('au'))
    print(solution.lengthOfLongestSubstring(' '))
    print(solution.lengthOfLongestSubstring('bbbbbbb'))
