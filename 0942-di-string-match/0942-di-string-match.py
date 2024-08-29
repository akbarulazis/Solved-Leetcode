class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        res = []
        
        for i in s :
            if i == 'I':
                res.append(low)
                low = low + 1
            else:
                res.append(high)
                high = high - 1
        res.append(low)
        
        return res