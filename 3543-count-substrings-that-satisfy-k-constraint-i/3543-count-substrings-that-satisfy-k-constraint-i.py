class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        count = 0

        for x in range(n):
            zeros = 0
            ones = 0
            for y in range(x,n):
                if s[y] == '0':
                    zeros += 1
                else:
                    ones += 1

                if ones <= k or zeros <= k:
                    count += 1
        
        return count