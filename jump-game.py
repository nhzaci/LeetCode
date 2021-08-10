class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # time complexity: O(n) -> n iteration depth
        # space complexity: O(1) -> no extra memory required
        max_idx = 0
        for i, jump_dist in enumerate(nums):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + jump_dist)
        return True
