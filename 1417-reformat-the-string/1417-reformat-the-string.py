class Solution:
    def reformat(self, s: str) -> str:
        if len(s)==1:
            return s
        if s.isnumeric() or s.isalpha():
            return ''
        alpha = []
        num = []
        res = []
        
        for x in s:
            if x.isalpha():
                alpha.append(x)
            elif x.isnumeric:
                num.append(x)
        if ( len(num) > len(alpha) + 1 ) or ( len(alpha) > len(num) + 1 ) :
            return ''
        elif len(num) > len(alpha):
            res.append(num[0])
            for x in range(len(num)-1):
                res.append(alpha[x])
                res.append(num[x+1])
        elif len(alpha) > len(num):
            res.append(alpha[0])
            for x in range(len(alpha)-1):
                res.append(num[x])
                res.append(alpha[x+1])
        elif len(alpha) == len(num):
            for x in range(len(num)):
                res.append(alpha[x])
                res.append(num[x])
        
        return ''.join(res)
                
        
        