# question from thread: https://leetcode.com/discuss/interview-question/354563/google-phone-screen-delete-islands
def delete_islands(islands: list[list[int]]) -> list[list[int]]:
    # n = rows
    # m = cols
    # time complexity: O(n * m) -> iterate through whole graph at worst
    # space complexity: O(n * m) -> recursive stack max recursion is whole graph
    def dfs(row, col, islands, visited, to_delete, ROWS, COLS):
        # check regular dfs bounds
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or visited[row][col] or islands[row][col] == 0:
            return

        visited[row][col] = True

        # create directions array to check above, below, left or right of current position
        directions = [(row + 1, col), (row, col + 1),
                      (row - 1, col), (row, col - 1)]
        # check if any of the indices are out of bounds in row or col
        if len(list(filter(lambda x: x[0] < 0 or x[1] < 0 or x[0] >= ROWS or x[1] >= COLS, directions))) == 0:
            # start with is_surrounded
            is_surrounded = True
            for new_row, new_col in directions:
                # if any of the points directly adjacent are != 1, then it's not surrounded
                if islands[new_row][new_col] != 1:
                    is_surrounded = False
                    # break early
                    break
            # if is_surrounded, append the row and col to delete
            if is_surrounded:
                to_delete.append((row, col))

        # regular dfs operation here
        dfs(row + 1, col, islands, visited, to_delete, ROWS, COLS)
        dfs(row - 1, col, islands, visited, to_delete, ROWS, COLS)
        dfs(row, col + 1, islands, visited, to_delete, ROWS, COLS)
        dfs(row, col - 1, islands, visited, to_delete, ROWS, COLS)
    # predefine these so we get less confused and also don't have to recalculate
    ROWS = len(islands)
    COLS = len(islands[0])
    # make visited array
    visited = [[False for i in range(COLS)] for i in range(ROWS)]
    # store coordinates to be flipped to 0 in the end
    to_delete = []
    # iterate and dfs through graph
    for row in range(ROWS):
        for col in range(COLS):
            if not visited[row][col]:
                dfs(row, col, islands, visited, to_delete, ROWS, COLS)

    # for the results in to_delete, we flip them in-place
    for row, col in to_delete:
        islands[row][col] = 0
    # return initial graph, but actually done in place anyway
    return islands


print(delete_islands([[0, 0, 0, 1, 1, 1],
                      [0, 0, 0, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1]]))

print(delete_islands([[1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1]]))

print(delete_islands([[1, 1, 1, 0, 1, 1, 1],
                      [1, 1, 1, 0, 1, 1, 1],
                      [1, 1, 1, 0, 1, 1, 1],
                      [0, 0, 0, 0, 1, 1, 1],
                      [1, 1, 1, 0, 1, 1, 1]]))
