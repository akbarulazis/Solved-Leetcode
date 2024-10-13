class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t1 = list(t)
        t2 = []
        t3 = 0
        for x in list(s):
            if x in ''.join(t1):
                ind = t1.index(x)
                del t1[:ind+1]
                t3 += 1

            else:
                return False
        if t3 == len(s):
            return True
        else:
            return False