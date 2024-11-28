class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        k = list(s)
        for x in k:
            if stack and abs(ord(stack[-1]) - ord(x)) == 32:
                stack.pop()
            else:
                stack.append(x)
        
        return ''.join(stack)
        