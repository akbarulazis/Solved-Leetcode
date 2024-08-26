
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new_heights = sorted(heights)
        new_heights.reverse()
        res = []
        for i in new_heights:
            x = heights.index(i)
            res.append(names[x])
        return res