class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        prev_count = 0
        path_len = {}

        for line in input.split('\n'):
            count = line.count('\t')
            path_len[count] = len(line) - count
            if '.' in line:
                max_len = max(max_len, sum([path_len[i]
                                            for i in range(count + 1)]) + count)
        return max_len
