class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time complexity: O(n ** 2)
        # space complexity: O(n)
        def helper(nums, start, memo):
            if start == 0:
                return 1

            curr = nums[start]
            max_val = 0
            # O(n) to iterate through all previous points to find max
            for idx in range(start - 1, -1, -1):  # from start to 0
                value = nums[idx]
                if curr > value:
                    max_val = max(max_val, memo[idx])
            # memoize current value!
            memo[start] = max_val + 1
            return memo[start]
        max_count = 0
        # O(n) space for memo array
        memo = [1 for i in range(len(nums))]
        # O(n) loop
        for i in range(len(nums)):
            max_count = max(helper(nums, i, memo), max_count)
        return max_count
