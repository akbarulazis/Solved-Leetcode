class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        k = {}
        res = []
        for x in range(len(s)):
            k[indices[x]] = s[x]
        indices.sort()
        for x in indices:
            res.append(k[x])
        
        return ''.join(res)
        
        
        