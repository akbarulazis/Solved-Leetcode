class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        k=0
        for x in range(len(s)+1):
            if s[k:x].count('R') == s[k:x].count('L') and s[k:x] != '':
                k = x
                res += 1
        return res