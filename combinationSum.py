class Solution:
    def combinationSum(self, candidates, target: int):
        results = []
        candidates.sort()

        def dfs(array, target_to_hit):
            if target_to_hit == 0:
                results.append(array)
                return
            for candidate in candidates:
                if candidate > target_to_hit:
                    break
                elif len(array) == 0 or candidate >= array[-1]:
                    dfs(array + [candidate], target_to_hit - candidate)
        dfs([], target)
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([2, 3, 5], 8))
