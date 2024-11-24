from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        k = Counter(text)
        req = {'b':1,'a':1,'l':2,'o':2,'n':1}
        
        mi = float('inf')
        for char, num in req.items():
            mi = min(mi, k[char]//num)
        
        return mi