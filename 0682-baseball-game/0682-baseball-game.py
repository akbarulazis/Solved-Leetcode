class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in operations:
            try:
                int(i)
                is_dig = True
            except ValueError:
                is_dig = False
            if is_dig:
                res.append(int(i))
            elif i == 'C':
                res.pop()
            elif i == 'D':
                d = res[-1]*2
                res.append(d)
            elif i == '+':
                plus = res[-1] + res[-2]
                res.append(plus)
        if len(res) == 0:
            return 0
        else:
            return sum(res)