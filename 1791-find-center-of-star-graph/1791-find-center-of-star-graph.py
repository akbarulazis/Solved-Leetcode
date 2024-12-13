from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        k = [str(x) for words in edges for x in words]
        coun = Counter(k)
        for a,b in coun.items():
            if b == n:
                return int(a)
        