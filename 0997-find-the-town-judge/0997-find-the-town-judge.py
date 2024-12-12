class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num = [0]*(n+1)
        if len(trust) == 0 and n == 1:
            return n
        for a,b in trust:
            num[a] -= 1
            num[b] += 1

        for i in range(n+1):
            if num[i] == (n-1):
                return i
        
        return -1
        