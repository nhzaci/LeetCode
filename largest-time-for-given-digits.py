class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def permutations(lst):
            if len(lst) == 1:
                return [lst[:]]
            else:
                results = []
                for i in range(len(lst)):
                    n = lst.pop(0)
                    perms = permutations(lst)
                    
                    for perm in perms:
                        perm += [n]
                    
                    results += perms
                    
                    lst += [n]
                return results
        def filter_invalid_time(t):
            if t[0] * 10 + t[1] < 24 and t[2] < 6:
                return True
            return False
        filtered_lst = list(filter(filter_invalid_time, sorted(permutations(arr), reverse=True)))
        if not len(filtered_lst):
            return ''
        h1, h2, m1, m2 = filtered_lst[0]
        return f'{h1}{h2}:{m1}{m2}'
