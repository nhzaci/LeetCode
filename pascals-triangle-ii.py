class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # time complexity: O(rowIndex) -> total number of iterations
        # space complexity: O(1) -> no extra space required
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        prev = [1, 1]

        for currRowIndex in range(1, rowIndex + 1):
            new = [1 for i in range(currRowIndex + 1)]
            for i in range(1, currRowIndex):
                new[i] = prev[i] + prev[i - 1]
            prev = new
        return new
