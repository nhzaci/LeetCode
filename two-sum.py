class Solution:
    def twoSum(self, nums, target: int):
        '''
        Use a hashtable storing an array of indices with keys being the value of item in nums
        If there are more than one key in the array, use the key that is not equal to the current index
        Time complexity: O(n)
        '''
        # initialize dictionary
        hashtable = {}

        # init hashtable
        for (index, item) in enumerate(nums):
            if item in hashtable:
                hashtable[item].append(index)
            else:
                hashtable[item] = [index]

        # check if difference between sum and target can be found on hash table
        for (index, item) in enumerate(nums):
            diff = target - item
            if diff in hashtable:
                for idx in hashtable[target - item]:
                    if idx != index:
                        return [index, idx]

    def twoSum2(self, nums, target: int):
        '''
        Second solution 
        Time: O(n log n) -> Merge sort time complexity
        '''
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum < target:
                right -= 1
            elif curr_sum > target:
                left += 1
            else:
                return [left, right]

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
