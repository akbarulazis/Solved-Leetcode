class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        te = text.split(" ")
        for x in range(2,len(te)):
            if te[x-2] == first and te[x-1] == second:
                res.append(te[x])
        return res