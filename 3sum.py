class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n log n) sorting
        nums.sort()
        results = []
        # take i as pivot element
        for start in range(len(nums) - 2):
            if start > 0 and nums[start] == nums[start - 1]:
                continue

            left = start + 1
            right = len(nums) - 1
            
            while left < right:
                curr_sum = nums[start] + nums[left] + nums[right] 
                
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    results.append([nums[start], nums[left], nums[right]])
                    # eliminate duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return results
