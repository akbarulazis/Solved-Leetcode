class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        for x in s:
            if x == ')':
                temporaryList = []

                while res and res[-1] != '(':
                    temporaryList.append(res.pop())
                
                res.pop()
                res = res + temporaryList
            else:
                res.append(x)
        
        return ''.join(res)