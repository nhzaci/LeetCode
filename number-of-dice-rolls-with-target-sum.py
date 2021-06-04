class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MODULO = 10 ** 9 + 7
        memo = {}
        
        def numRollsAndTarget(no_rolls, no_faces, target):
            nonlocal memo
            if not no_rolls and not target:
                return 1
            elif not no_rolls and target:
                return 0
            else:
                if (no_rolls, no_faces, target) in memo:
                    return memo[(no_rolls, no_faces, target)]
                else:
                    result = 0
                    for face in range(1, no_faces + 1):
                        result += numRollsAndTarget(
                            no_rolls - 1, 
                            no_faces,
                            target - face)
                    memo[(no_rolls, no_faces, target)] = result
                    return result
        
        return numRollsAndTarget(d, f, target) % MODULO
