class Solution:
    def convertDateToBinary(self, date: str) -> str:
        res = []
        k = date.split('-')
        for x in k:
            res.append(bin(int(x))[2:])
        return '-'.join(res)