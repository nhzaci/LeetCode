class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        indices_to_mutate = []
        idx_offset = 0

        # iterate through nums
        for (idx, num) in enumerate(nums):
            print(idx)
            if num == val:
                indices_to_mutate.append(idx)
                count -= 1

        # mutate elems
        for idx in indices_to_mutate:
            nums.pop(idx - idx_offset)
            idx_offset += 1

        return count

    # my second attempt
    def removeElement2(self, nums: List[int], val: int) -> int:
        # [3, 2, 2, 3, 4], val = 3
        # offset = 0
        # when i = 0, we find 3, increment offset,
        # offset = 1
        # when i = 1, we find 2, we shift 2 by offset of 1,
        # nums = [2, 2, 2, 3, 4]
        # when i = 2, we find 2, we shift 2 by offset of 1
        # nums = [2, 2, 2, 3, 4]
        # when i = 3, we find 3, increment offset
        # offset = 2
        # when i = 4, we find 4, shift 4 by offset of 2
        # nums = [2, 2, 4, _, _]
        offset = 0
        for idx, num in enumerate(nums):
            if num == val:
                offset += 1
            else:
                nums[idx - offset] = num
        return len(nums) - offset
