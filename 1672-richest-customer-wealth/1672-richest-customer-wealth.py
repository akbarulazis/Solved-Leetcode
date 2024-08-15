class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        for x in accounts:
            res.append(sum(x))
        res.sort()
        return res[-1]
        