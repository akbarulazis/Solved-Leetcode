class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = []
        for i in range(len(s)):
            ind = t.find(s[i])
            res.append(abs(i-ind))
        return sum(res)
        