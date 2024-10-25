class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s = list(s)
        p = [x for x in range(len(s)) if s[x] == c]
        res = []
        
        for x in range(len(s)):
            k = []
            for y in p:
                k.append(abs(x-y))
            res.append(min(k))
            
        # print(k)
        return res