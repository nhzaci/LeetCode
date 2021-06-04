class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Faster than 90.78% of solutions
        Use dictionary in order to cache elements already found in list for O(1) query, if hit, return True
        If iterated through list and no hit, return False
        Time complexity: O(n)
        Space Complexity: O(n)
        where n is the length of list nums
        '''
        elements = {}
        for num in nums:
            if num in elements:
                return True
            elements[num] = 1
        return False
