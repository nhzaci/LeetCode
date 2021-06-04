class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(lst):
            # base case
            if len(lst) == 1:
                return [lst[:]]
            
            results = []
            for i in range(len(lst)):
                n = lst.pop(0)
                perms = recur(lst)
                
                for perm in perms:
                    perm += [n]                
                    
                results += perms
                
                lst += [n]            
            return results
        return recur(nums)
