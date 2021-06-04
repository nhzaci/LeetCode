class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distToOrigin(p):
            x, y = p
            return math.sqrt(x ** 2 + y ** 2)
        return list(map(lambda idxDist: points[idxDist[0]], sorted(map(lambda idxPt: (idxPt[0], distToOrigin(idxPt[1])), enumerate(points)), key=lambda x:x[1])))[:k]
