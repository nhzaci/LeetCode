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
