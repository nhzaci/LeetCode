class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        noCandies = len(candyType) // 2
        uniqueCandies = set(candyType)
        return min(noCandies, len(uniqueCandies))
