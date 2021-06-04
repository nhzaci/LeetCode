class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1 if nums[1] > nums[0] else 0
        
        ptr = 0
        while ptr <= len(nums) - 2:
            # edge case, at first element
            if ptr == 0:
                if nums[ptr] > nums[ptr + 1]:
                    return ptr
            else:
                # check both sides
                if nums[ptr] > nums[ptr + 1] and nums[ptr] > nums[ptr - 1]:
                    return ptr
                
            ptr += 1
        # edge case last element is peak
        if nums[-1] > nums[-2]:
            return len(nums) - 1
