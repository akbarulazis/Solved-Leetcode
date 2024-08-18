class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        for poin in points:
            x.append(poin[0])
        x.sort()
        k = []
        for i in range(len(x)-1):
            k.append(x[i+1] - x[i])
        return max(k)