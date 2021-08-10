class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_tail = 0
        prev = None

        for idx, num in enumerate(nums):
            if prev == None:
                prev = num
                new_tail += 1
            else:
                if prev != num:
                    nums[new_tail] = num
                    new_tail += 1
                    prev = num

        return new_tail
