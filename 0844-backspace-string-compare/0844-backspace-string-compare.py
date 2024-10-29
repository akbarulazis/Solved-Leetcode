class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def stacking(s):
            stack = []
            
            for x in s:
                if x == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(x)
            return ''.join(stack)
        return stacking(s) == stacking(t)
            