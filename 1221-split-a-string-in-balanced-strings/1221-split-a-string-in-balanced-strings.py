class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # res = 0
        # k=0
        # for x in range(len(s)+1):
        #     if s[k:x].count('R') == s[k:x].count('L') and s[k:x] != '':
        #         k = x
        #         res += 1
        # return res
        
        res = 0
        count = 0
        
        for char in s:
            if char == 'L':
                count+= 1
            else:
                count -= 1
            if count == 0:
                res += 1
        
        return res