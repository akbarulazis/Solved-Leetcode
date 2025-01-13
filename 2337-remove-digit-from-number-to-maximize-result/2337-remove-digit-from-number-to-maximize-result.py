class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        num= [x for x in number]
        res = []
        for x in range(len(num)):
            if num[x] == digit:
                y = num.copy()
                y.pop(x)
                res.append(int(''.join(y)))

        return str(max(res))