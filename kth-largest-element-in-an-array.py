class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            curr_largest = nums[i]
            largest_idx = i
            for j in range(i, len(nums)):
                potential = nums[j]
                if potential > curr_largest:
                    curr_largest = potential
                    largest_idx = j
            nums[i], nums[largest_idx] = nums[largest_idx], nums[i]
        return nums[k - 1]
