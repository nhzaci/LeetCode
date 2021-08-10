class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, results, curr, target):
            if target == 0:
                results.append(curr)
                return
            elif target < 0:
                return

            for candidate in candidates:
                if candidate > target:
                    break
                if len(curr) == 0 or candidate >= curr[-1]:
                    dfs(candidates, results,
                        curr[:] + [candidate], target - candidate)

        candidates.sort()
        results = []
        dfs(candidates, results, [], target)
        return results
