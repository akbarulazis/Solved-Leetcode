class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balance = 0
        for x in s:
            if x == '(':
                if balance > 0:
                    res.append(x)
                balance += 1
            elif x == ')':
                balance -= 1
                if balance > 0:
                    res.append(x)
        
        
        return ''.join(res)